import os
import warnings

import pandas as pd
from prophet import Prophet


warnings.filterwarnings("ignore")
import pandas_datareader.data as web
from pandas_datareader import data
import yfinance as yf
yf.pdr_override() # TypeError: string indices must be integers 해결법
path = "c:/Windows/Fonts/malgun.ttf"
import platform
from matplotlib import font_manager, rc, pyplot as plt

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')
plt.rcParams['axes.unicode_minus'] = False

'''
Date Open     High      Low    Close     Adj Close   Volume
'''
root = r'C:\Users\최민호\PycharmProjects\AIacademy-django-react\djangoProject\kia_stock'
class AiTraderService(object):

    def __init__(self):
        global start_date, end_date, item_code
        start_date = "2019-1-4"
        end_date = '2022-12-30'
        item_code = '000270.KS'

    def hook(self):
        item = data.get_data_yahoo(item_code, start_date, end_date)
        print(f" KIA head: {item.head(3)}")
        print(f" KIA tail: {item.tail(3)}")
        item['Close'].plot(figsize=(12,6), grid=True)
        item_trunc = item[:'2021-12-31']
        df = pd.DataFrame({'ds': item_trunc.index, 'y': item_trunc['Close']})
        df.reset_index(inplace=True)
        del df['Date']
        prophet = Prophet(daily_seasonality=True)
        prophet.fit(df)
        future = prophet.make_future_dataframe(periods=61)
        forecast = prophet.predict(future)
        prophet.plot(forecast)
        plt.figure(figsize=(12,6))
        plt.plot(item.index, item['Close'], label='real')
        plt.plot(forecast['ds'], forecast['yhat'], label='forecast')
        plt.grid()
        plt.legend()
        plt.savefig(os.path.join(root, 'kia_close.png'))



if __name__ == '__main__':
    ai = AiTraderService()
    ai.hook()








# class AiTraderService(object):
#     def __init__(self, state_size, action_space = 3, model_name = "AiTrader"):
#         self.state_size = state_size
#         self.action_space = action_space
#         self.model_name = model_name
#         self.memory = deque(maxlen=2000)
#         self.gamma = 0.95
#         self.epsilon = 1.0
#         self.epsilon_final = 0.01
#         self.epsilon_decay = 0.995
#         self.model = self.model_builder()
#
#     def model_builder(self):
#         model = tf.keras.models.Sequential()
#         model.add(tf.keras.layers.Dense(units=32, activation='relu', input_dim=self.state_size))
#         model.add(tf.keras.layers.Dense(units=64, activation='relu'))
#         model.add(tf.keras.layers.Dense(units=128, activation='relu'))
#         model.add(tf.keras.layers.Dense(units=self.action_space, activation='linear'))
#         model.compile(loss='mse',optimizer=tf.keras.optimizers.Adam(lr=0.01))
#         return model
#
#     def trade(self, state):
#         if random.random() <= self.epsilon:
#             return random.randrange(self.action_space)
#         actions = self.model.predict(state)
#         return np.argmax(actions[0])
#
#     def batch_train(self, batch_size):
#         batch = []
#         for i in range(len(self.memory) - batch_size +1, len(self.memory)):
#             batch.append(self.memory[i])
#         for state, action, reward, next_state, done in batch:
#             reward = reward
#             if not done:
#                 reward = reward + self.gamma * np.amax(self.model.predict(next_state)[0])
#             target = self.model.predict(state)
#             target[0][action] = reward
#             self.model.fit(state, target, epochs=1, verbose=0)
#
#         if self.epsilon > self.epsilon_final:
#             self.epsilon *= self.epsilon_decay
# class Trading:
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def sigmoid(x):
#         return 1 / (1 + math.exp(-x))
#
#     @staticmethod
#     def stock_price_format(n):
#         if n < 0:
#             return "- ${0:2f}".format(abs(n))
#         else:
#             return "${0:2f}".format(abs(n))
#     @staticmethod
#     def dataset_loader(stock_name):
#         dataset = data_reader.DataReader(stock_name, data_source="yahoo")
#         start_date = str(dataset.index[0]).split()[0]
#         end_date = str(dataset.index[-1]).split()[0]
#         close = dataset['Close']
#         return close
#
#     def state_creator(self, data, timestep, window_size):
#         starting_id = timestep - window_size + 1
#         if starting_id >= 0:
#             windowed_data = data[starting_id: timestep + 1]
#         else:
#             windowed_data =- starting_id * [data[0]] + list(data[0:timestep+1])
#
#         state = []
#         for i in range(window_size -1):
#             state.append(self.sigmoid(windowed_data[i + 1] - windowed_data[i]))
#         return np.array([state])
#
#     def transaction(self, target):
#         stock_name = target
#         data = self.dataset_loader(stock_name)
#         window_size = 10
#         episodes = 1000
#         batch_size = 32
#         data_samples = len(data) -1
#         trader = AiTrader(window_size)
#         print('===== Model Summary =======')
#         print(trader.model.summary())
#         for episode in range(1, episodes + 1):
#             print('EPISODE: {}/{}'.format(episode, episodes))
#             state = self.state_creator(data, 0, window_size + 1)
#             total_profit  = 0
#             trader.inventory = []
#             for t in tqdm(range(data_samples)):
#                 action = trader.trade(state)
#                 next_state = self.state_creator(data, t + 1, window_size + 1)
#                 reward = 0
#                 if action == 1: # Buying
#                     trader.inventory.append(data[t])
#                     print('AI트레이더 매수 : ', self.stock_price_format(data[t]))
#                 elif action ==2 and len(trader.inventory) > 0: # Selling
#                     buy_price = trader.inventory.pop(0)
#                     reward = max(data[t] - buy_price, 0)
#                     total_profit += data[t] - buy_price
#                     print('AI트레이더 매도 : ', self.stock_price_format(data[t]),
#                           ', 이익: '+self.stock_price_format(data[t] - buy_price))
#                 if t == data_samples - 1:
#                     done = True
#                 else:
#                     done = False
#                 trader.memory.append((state, action, reward, next_state, done))
#                 state = next_state
#
#                 if done:
#                     print('###############')
#                     print('총이익 : {}'.format(total_profit))
#                     print('###############')
#                 if len(trader.memory) > batch_size:
#                     trader.batch_train(batch_size)
#             if episode % 10 == 0:
#                 trader.model.save('ai_trader_{}.h5'.format(episode))
#
#
# if __name__ == '__main__':
#     t = Trading()
#     t.transaction('AAPL')