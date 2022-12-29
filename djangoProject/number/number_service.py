import numpy as np
import pandas as pd
import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from keras.saving.save import load_model
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
import os

from tensorflow import keras

class NumberService(object):
    def __init__(self):
        global class_names
        class_names = ['0', '1', '2', '3', '4',
                       '5', '6', '7', '8', '9']

    # self, i, predictions_array, true_label, img
    def service_model(self, i) -> '':
        model = load_model(r"C:\Users\AIA\PycharmProjects\djangoProject\number\save\number_model.h5")
        (train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()

        x_train, x_test = train_images / 255.0, test_images / 255.0


        predictions = model.predict(x_test)
        predictions_array, true_label, img = predictions[i], test_labels[i], x_test[i]
        '''
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img, cmap=plt.cm.binary)
        '''
        result = np.argmax(predictions_array)
        # print(f"예측한 답 : {result}")
        '''
        if predicted_label == true_label:
            color = 'blue'
        else:
            color = 'red'

        plt.xlabel('{} {:2.0f}% ({})'.format(
            class_names[predicted_label],
            100 * np.max(predictions_array),
            class_names[true_label]
        ), color = color)
        plt.show()
        '''
        if result == 0:
            resp = '숫자0'
        elif result == 1:
            resp = '숫자1'
        elif result == 2:
            resp = '숫자2'
        elif result == 3:
            resp = '숫자3'
        elif result == 4:
            resp = '숫자4'
        elif result == 5:
            resp = '숫자5'
        elif result == 6:
            resp = '숫자6'
        elif result == 7:
            resp = '숫자7'
        elif result == 8:
            resp = '숫자8'
        elif result == 9:
            resp = '숫자9'
        print(f"넘버 서비스에서 예측한 값: {resp}")
        return resp




    @staticmethod
    def plot_value_array(i, predictions_array, true_label):
        predictions_array, true_label = \
            predictions_array[i], true_label[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        thisplot = plt.bar(range(10),
                           predictions_array,
                           color='#777777')
        plt.ylim([0, 1])
        predicted_label = np.argmax(predictions_array)
        thisplot[predicted_label].set_color('red')
        thisplot[true_label].set_color('blue')



iris_menu = ["Exit",  # 0
               "Learning",  # 1
               ]

iris_lambda = {
    "1": lambda x: x.service_model(),
    }

if __name__ == '__main__':
    ir = NumberService()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(iris_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                iris_lambda[menu](ir)
            except:

                print("Didn't catch error message")