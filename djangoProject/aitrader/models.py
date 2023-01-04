import os.path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.callbacks import EarlyStopping

from keras.models import Sequential
from keras.callbacks import EarlyStopping
from enum import Enum
from keras.models import Model
from keras.layers import Dense, Input
from keras.layers import concatenate
from keras.layers import Dense, LSTM
from abc import abstractmethod, ABCMeta
root = r"C:\Users\최민호\PycharmProjects\AIacademy-django-react\djangoProject"

# 데이터 전처리 및 npy 저장
def save_npy():
    kospi_csv = pd.read_csv(os.path.join(root, "aitrader", "data", "kospi.csv"),
                            index_col=0, header=0, encoding='utf-8', sep=',')
    samsung_csv = pd.read_csv(os.path.join(root, "aitrader", "data", "samsung.csv"),
                              index_col=0, header=0, encoding='utf-8', sep=',')
    loop= 0
    for d in [kospi_csv, samsung_csv]:
        del d['변동 %']
        d = d.astype('str')
        d.replace(np.nan, '0', regex=True, inplace=True)
        d = d[d['거래량'] != '0']
        for i in range(len(d.index)):
            for j in range(len(d.iloc[i])):
                if d.iloc[i, j][-1] == "M":
                    d.iloc[i, j] = d.iloc[i, j].replace(',', '')
                    d.iloc[i, j] = d.iloc[i, j].replace('M', '')
                    d.iloc[i, j] = float(d.iloc[i, j])
                    d.iloc[i, j] = d.iloc[i, j] * 1000000
                elif d.iloc[i, j][-1] == "K":
                    d.iloc[i, j] = d.iloc[i, j].replace(',', '')
                    d.iloc[i, j] = d.iloc[i, j].replace('K', '')
                    d.iloc[i, j] = float(d.iloc[i, j])
                    d.iloc[i, j] = d.iloc[i, j] * 1000
                else:
                    d.iloc[i, j] = d.iloc[i, j].replace(',', '')
                    d.iloc[i, j] = float(d.iloc[i, j])
        d.sort_values(['날짜'], ascending=[True], inplace=True)
        d = d.values
        print(type(d))
        print(d.shape)
        loop += 1
        if loop == 1: np.save(os.path.join(root, "aitrader", "save", "kospi.npy"), arr=d)
        elif loop == 2: np.save(os.path.join(root, "aitrader", "save", "samsung.npy"), arr = d)

######################################################################################################

class ModelType(Enum): # 상수 풀
    dnn_model = 1
    dnn_ensemble = 2
    lstm_model = 3
    lstm_ensemble = 4

class H5FileNames(Enum):
    dnn_model = "samsung_stock_dnn_model.h5"
    dnn_ensemble = "samsung_stock_dnn_ensemble.h5"
    lstm_model = "samsung_stock_lstm_model.h5"
    lstm_ensemble = "samsung_stock_lstm_ensemble.h5"


class AiTradeBase(metaclass=ABCMeta): # 추상 클래스
    @abstractmethod
    def split_xy5(self, **kwargs): pass

    @abstractmethod
    def create(self): pass

    @abstractmethod
    def basic_scaled(self): pass

    @abstractmethod
    def basic_fit(self): pass

    @abstractmethod
    def ensemble_scaled(self): pass

    @abstractmethod
    def ensemble_fit(self): pass

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

    def create(self):
        pass
    def basic_scaled(self):
        x, y = self.split_xy5(dataset=samsung, time_steps=5, y_column=1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        x_train = np.reshape(x_train,
                             (x_train.shape[0], x_train.shape[1] * x_train.shape[2]))
        x_test = np.reshape(x_test,
                            (x_test.shape[0], x_test.shape[1] * x_test.shape[2]))
        scaler = StandardScaler()
        scaler.fit(x_train)
        x_train_scaled = scaler.transform(x_train)
        x_test_scaled = scaler.transform(x_test)
        return x_test_scaled, x_train_scaled, y_test, y_train

    def basic_fit(self, model, x_test_scaled, x_train_scaled, y_test, y_train):
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))
        model.compile(loss='mse', optimizer='adam', metrics=['mse'])
        early_stopping = EarlyStopping(patience=20)
        x_train_scaled = x_train_scaled.astype(np.float32)
        x_test_scaled = x_test_scaled.astype(np.float32)
        y_train = y_train.astype(np.float32)
        y_test = y_test.astype(np.float32)
        model.fit(x_train_scaled, y_train, validation_split=0.2, verbose=1,
                  batch_size=1, epochs=100, callbacks=[early_stopping])
        loss, mse = model.evaluate(x_test_scaled, y_test, batch_size=1)
        print('loss : ', loss)
        print('mse : ', mse)
        return x_test_scaled, y_test

    def ensemble_scaled(self):
        x1, y1 = self.split_xy5(dataset=samsung,
                                time_steps=5,
                                y_column=1)
        x2, y2 = self.split_xy5(dataset=kospi200,
                                time_steps=5,
                                y_column=1)
        x1_train, x1_test, y1_train, y1_test = train_test_split(
            x1, y1, random_state=1, test_size=0.3)
        x2_train, x2_test, y2_train, y2_test = train_test_split(
            x2, y2, random_state=2, test_size=0.3)
        x1_train = np.reshape(x1_train,
                              (x1_train.shape[0], x1_train.shape[1] * x1_train.shape[2]))
        x1_test = np.reshape(x1_test,
                             (x1_test.shape[0], x1_test.shape[1] * x1_test.shape[2]))
        x2_train = np.reshape(x2_train,
                              (x2_train.shape[0], x2_train.shape[1] * x2_train.shape[2]))
        x2_test = np.reshape(x2_test,
                             (x2_test.shape[0], x2_test.shape[1] * x2_test.shape[2]))
        scaler1 = StandardScaler()
        scaler1.fit(x1_train)
        x1_train_scaled = scaler1.transform(x1_train)
        x1_test_scaled = scaler1.transform(x1_test)
        scaler2 = StandardScaler()
        scaler2.fit(x2_train)
        x2_train_scaled = scaler2.transform(x2_train)
        x2_test_scaled = scaler2.transform(x2_test)
        return x1_test_scaled, x1_train_scaled, x2_test_scaled, x2_train_scaled, y1_test, y1_train

    def ensemble_fit(self, dense2, input1, input2, output1, x1_test_scaled, x1_train_scaled, x2_test_scaled,
                     x2_train_scaled, y1_test, y1_train):
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        output2 = Dense(32)(dense2)
        merge = concatenate([output1, output2])
        output3 = Dense(1)(merge)
        model = Model(inputs=[input1, input2],
                      outputs=output3)
        model.compile(loss='mse', optimizer='adam', metrics=['mse'])
        early_stopping = EarlyStopping(patience=20)
        x1_train_scaled = x1_train_scaled.astype(np.float32)
        x1_test_scaled = x1_test_scaled.astype(np.float32)
        x2_train_scaled = x2_train_scaled.astype(np.float32)
        x2_test_scaled = x2_test_scaled.astype(np.float32)
        y1_train = y1_train.astype(np.float32)
        y1_test = y1_test.astype(np.float32)
        model.fit([x1_train_scaled, x2_train_scaled], y1_train, validation_split=0.2,
                  verbose=1, batch_size=1, epochs=100,
                  callbacks=[early_stopping])
        loss, mse = model.evaluate([x1_test_scaled, x2_test_scaled], y1_test, batch_size=1)
        print('loss : ', loss)
        print('mse : ', mse)
        return model, x1_test_scaled, x2_test_scaled, y1_test

class DnnModel(AiTraderModel):

    def create(self):
        x_test_scaled, x_train_scaled, y_test, y_train = self.basic_scaled()

        model = Sequential()
        model.add(Dense(64, input_shape=(25,)))
        x_test_scaled, y_test = self.basic_fit(model, x_test_scaled, x_train_scaled, y_test, y_train)

        y_pred = model.predict(x_test_scaled)
        for i in range(5):
            print('종가 : ', y_test[i], '/ 예측가 : ', y_pred[i])

        file_name = os.path.join(os.path.abspath("save"), H5FileNames.dnn_model.value)
        model.save(file_name)

class DnnEnsemble(AiTraderModel):

    def create(self):
        x1_test_scaled, x1_train_scaled, x2_test_scaled, x2_train_scaled, y1_test, y1_train = self.ensemble_scaled()

        input1 = Input(shape=(25,))
        dense1 = Dense(64)(input1)
        dense1 = Dense(32)(dense1)
        dense1 = Dense(32)(dense1)
        output1 = Dense(32)(dense1)

        input2 = Input(shape=(25,))
        dense2 = Dense(64)(input2)
        model, x1_test_scaled, x2_test_scaled, y1_test = self.ensemble_fit(dense2, input1, input2, output1,
                                                                           x1_test_scaled, x1_train_scaled,
                                                                           x2_test_scaled, x2_train_scaled, y1_test,
                                                                           y1_train)

        y1_pred = model.predict([x1_test_scaled, x2_test_scaled])

        for i in range(5):
            print('종가 : ', y1_test[i], '/ 예측가 : ', y1_pred[i])

        file_name = os.path.join(os.path.abspath("save"), H5FileNames.dnn_ensemble.value)
        model.save(file_name)

class LstmModel(AiTraderModel):

    def create(self):
        x_test_scaled, x_train_scaled, y_test, y_train = self.basic_scaled()

        x_train_scaled = np.reshape(x_train_scaled,
                                    (x_train_scaled.shape[0], 5, 5))
        x_test_scaled = np.reshape(x_test_scaled,
                                   (x_test_scaled.shape[0], 5, 5))

        model = Sequential()
        model.add(LSTM(64, input_shape=(5, 5)))
        x_test_scaled, y_test = self.basic_fit(model, x_test_scaled, x_train_scaled, y_test, y_train)

        y_pred = model.predict(x_test_scaled)

        for i in range(5):
            print('종가 : ', y_test[i], '/ 예측가 : ', y_pred[i])

        file_name = os.path.join(os.path.abspath("save"), H5FileNames.lstm_model.value)
        model.save(file_name)

class LstmEnsemble(AiTraderModel):
    def create(self):
        x1_test_scaled, x1_train_scaled, x2_test_scaled, x2_train_scaled, y1_test, y1_train = self.ensemble_scaled()
        print(x2_train_scaled[0, :])

        x1_train_scaled = np.reshape(x1_train_scaled,
                                     (x1_train_scaled.shape[0], 5, 5))
        x1_test_scaled = np.reshape(x1_test_scaled,
                                    (x1_test_scaled.shape[0], 5, 5))
        x2_train_scaled = np.reshape(x2_train_scaled,
                                     (x2_train_scaled.shape[0], 5, 5))
        x2_test_scaled = np.reshape(x2_test_scaled,
                                    (x2_test_scaled.shape[0], 5, 5))

        input1 = Input(shape=(5, 5))
        dense1 = LSTM(64)(input1)
        dense1 = Dense(32)(dense1)
        dense1 = Dense(32)(dense1)
        output1 = Dense(32)(dense1)

        input2 = Input(shape=(5, 5))
        dense2 = LSTM(64)(input2)
        model, x1_test_scaled, x2_test_scaled, y1_test = self.ensemble_fit(dense2, input1, input2, output1,
                                                                           x1_test_scaled, x1_train_scaled,
                                                                           x2_test_scaled, x2_train_scaled, y1_test,
                                                                           y1_train)

        y1_pred = model.predict([x1_test_scaled, x2_test_scaled])

        for i in range(5):
            print('종가 : ', y1_test[i], '/ 예측가 : ', y1_pred[i])

        file_name = os.path.join(os.path.abspath("save"), H5FileNames.lstm_ensemble.value)
        model.save(file_name)

if __name__ == '__main__':
    # save_npy()
    # DnnModel().create()
    # DnnEnsemble().create()
    # LstmModel().create()
    LstmEnsemble().create()

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

DnnEnsemble
loss :  14726527.0
mse :  14726527.0
5/5 [==============================] - 0s 750us/step
종가 :  [64900.] / 예측가 :  [68650.6]
종가 :  [59000.] / 예측가 :  [59218.34]
종가 :  [72000.] / 예측가 :  [79147.81]
종가 :  [76800.] / 예측가 :  [77287.43]
종가 :  [83300.] / 예측가 :  [89430.484]

LstmModel
loss :  1156533.25
mse :  1156533.25
5/5 [==============================] - 0s 1ms/step
종가 :  [64900.] / 예측가 :  [65237.46]
종가 :  [59000.] / 예측가 :  [58876.324]
종가 :  [72000.] / 예측가 :  [73702.52]
종가 :  [76800.] / 예측가 :  [76877.77]
종가 :  [83300.] / 예측가 :  [82573.78]

LstmEnsemble
loss :  1184669.375
mse :  1184669.375
5/5 [==============================] - 1s 1000us/step
종가 :  [64900.] / 예측가 :  [64234.766]
종가 :  [59000.] / 예측가 :  [57992.277]
종가 :  [72000.] / 예측가 :  [72804.055]
종가 :  [76800.] / 예측가 :  [77710.02]
종가 :  [83300.] / 예측가 :  [83801.586]
'''