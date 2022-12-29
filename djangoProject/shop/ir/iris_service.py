import numpy as np
import pandas as pd
import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from keras.saving.save import load_model
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
class IrisService(object):
    def __init__(self):
        global model, graph, target_names
        model = load_model(r'C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\shop\ir\save\iris_model.h5')
        target_names = datasets.load_iris().target_names


    def service_model(self, features):
        features = np.reshape(features, (1, 4))
        Y_prob = model.predict(features, verbose=0)
        predicted = Y_prob.argmax(axis=-1) # argmax(axis=-1) 차원축소
        return predicted[0]  # p-value 가 가장 높은 것

    '''
    Shape (150, 6)
    'Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 
    'PetalWidthCm', 'Species'
    '''

iris_menu = ["Exit",  # 0
               "Learning",  # 1
               ]

iris_lambda = {
    "1": lambda x: x.service_model(),
    }

if __name__ == '__main__':
    ir = IrisService()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(iris_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                iris_lambda[menu](ir)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")