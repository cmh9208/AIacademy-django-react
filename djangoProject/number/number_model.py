import os

import keras.datasets.fashion_mnist
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder

class NumberModel(object):
    def __init__(self):
        pass

    def create_model(self):
        mnist = tf.keras.datasets.mnist
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0

        # plt.figure()
        # plt.imshow(train_images[10])
        # plt.colorbar()
        # plt.grid(False)
        # plt.show()
        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(512, activation=tf.nn.relu),
            tf.keras.layers.Dense(10, activation=tf.nn.softmax)
        ])

        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        model.fit(x_train, y_train, epochs=5)

        test_loss, test_acc = model.evaluate(x_test, y_test)
        print('테스트 정확도:', test_acc)
        file_name = os.path.join(os.path.abspath("save"), "number_model.h5")
        print(f"저장경로: {file_name}")
        model.save(file_name)




iris_menu = ["Exit",  # 0
               "Learning",  # 1
               ]

iris_lambda = {
    "1": lambda x: x.create_model(),
    }

if __name__ == '__main__':
    fs = NumberModel()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(iris_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                iris_lambda[menu](fs)
            except:
                print("Didn't catch error message")