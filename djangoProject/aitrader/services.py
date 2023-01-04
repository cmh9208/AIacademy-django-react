import os.path
import numpy as np
import pandas as pd
from keras.saving.save import load_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from keras.models import Sequential
from keras.callbacks import EarlyStopping
from enum import Enum
from keras.models import Model
from keras.layers import Dense, Input
from keras.layers import concatenate
from keras.layers import Dense, LSTM
from abc import abstractmethod, ABCMeta
root = r"C:\Users\최민호\PycharmProjects\AIacademy-django-react\djangoProject"

class ModelType(Enum):
    dnn_model = 1
    dnn_ensemble = 2
    lstm_model = 3
    lstm_ensemble = 4

class H5FileNames(Enum):
    dnn_model = "samsung_stock_dnn_model.h5"
    dnn_ensemble = "samsung_stock_dnn_ensemble.h5"
    lstm_model = "samsung_stock_lstm_model.h5"
    lstm_ensemble = "samsung_stock_lstm_ensemble.h5"

class AiTradeBase(metaclass=ABCMeta):
    @abstractmethod
    def split_xy5(self, **kwargs): pass

    @abstractmethod
    def create(self): pass

class AiTraderModel(AiTradeBase):

    def __init__(self):
        global path, kospi200, samsung
        kospi200 = np.load(os.path.join(root, "aitrader", "save", "kospi.npy"), allow_pickle=True)
        samsung = np.load(os.path.join(root, "aitrader", "save", "samsung.npy"), allow_pickle=True)
        print(kospi200)
        print(samsung)
        print(kospi200.shape)
        print(samsung.shape)

    def split_xy5(self, **kwargs):
        dataset = kwargs["dataset"]
        time_steps = kwargs["time_steps"]
        y_column = kwargs["y_column"]
        x, y = list(), list()
        for i in range(len(dataset)):
            x_end_number = i + time_steps
            y_end_number = x_end_number + y_column  # 수정

            if y_end_number > len(dataset):  # 수정
                break
            tmp_x = dataset[i:x_end_number, :]  # 수정
            tmp_y = dataset[x_end_number:y_end_number, 3]  # 수정
            x.append(tmp_x)
            y.append(tmp_y)
        return np.array(x), np.array(y)


class DnnModel(AiTraderModel):

    def create(self, i):
        x, y = self.split_xy5(dataset=samsung, time_steps=5, y_column=1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        x_train = np.reshape(x_train,
                             (x_train.shape[0], x_train.shape[1] * x_train.shape[2]))
        x_test = np.reshape(x_test,
                            (x_test.shape[0], x_test.shape[1] * x_test.shape[2]))
        scaler = StandardScaler()
        scaler.fit(x_train)
        x_test_scaled = scaler.transform(x_test)

        x_test_scaled = x_test_scaled.astype(np.float32)
        y_test = y_test.astype(np.float32)

        model = load_model(r'C:\Users\최민호\PycharmProjects\AIacademy-django-react\djangoProject\aitrader\save\samsung_stock_dnn_model.h5')
        y_pred = model.predict(x_test_scaled)
        # for i in range(5):
        #     print('종가 : ', y_test[i], '/ 예측가 : ', y_pred[i])


        # print('종가 : ', y_test[i], '/ 예측가 : ', y_pred[i])


        df = pd.read_csv(r'C:\Users\최민호\PycharmProjects\AIacademy-django-react\djangoProject\aitrader\data\samsung.csv')
        df2 = df[df['날짜'] == i]
        i = df2.index
        i = i[0]


        a, b = y_test[i], y_pred[i]
        a1, b1 = y_test[i-1], y_pred[i-1]
        a2, b2 = y_test[i-2], y_pred[i-2]
        a3, b3 = y_test[i-3], y_pred[i-3]
        a4, b4 = y_test[i-4], y_pred[i-4]

        a, b = str(a[0]), str(b[0])
        a1, b1 = str(a1[0]), str(b1[0])
        a2, b2 = str(a2[0]), str(b2[0])
        a3, b3 = str(a3[0]), str(b3[0])
        a4, b4 = str(a4[0]), str(b4[0])

        # print(a, b)
        # print(type(a), type(b))
        result = [f'종가 : {a}, / 예측가 : {b}',
                f'종가 : {a1}, / 예측가 : {b1}',
                f'종가 : {a2}, / 예측가 : {b2}',
                f'종가 : {a3}, / 예측가 : {b3}',
                f'종가 : {a4}, / 예측가 : {b4}']

        return result



if __name__ == '__main__':
    # save_npy()
    DnnModel().create()
    # DnnEnsemble().create()
    # LstmModel().create()
    # LstmEnsemble().create()

'''
DnnModel
loss :  985541.3125
mse :  985541.3125
5/5 [==============================] - 0s 500us/step
종가 :  [64900.] / 예측가 :  [64664.195]
종가 :  [59000.] / 예측가 :  [58412.402]
종가 :  [72000.] / 예측가 :  [72942.74]
종가 :  [76800.] / 예측가 :  [77117.336]
종가 :  [83300.] / 예측가 :  [82786.81]
'''