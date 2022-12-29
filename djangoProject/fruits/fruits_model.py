import os

import keras.datasets.fashion_mnist
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder

class FruitsModel(object):
    def __init__(self):
        pass

    def create_model(self):
        (train_images, train_labels), (test_images, test_labels) = keras.datasets.fashion_mnist.load_data()
        # plt.figure()
        # plt.imshow(train_images[10])
        # plt.colorbar()
        # plt.grid(False)
        # plt.show()
        model = Sequential([
            keras.layers.Flatten(input_shape=(28,28)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(10, activation='softmax')
        ])
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        model.fit(train_images, train_labels, epochs=5)
        test_loss, test_acc = model.evaluate(test_images, test_labels)
        print(f'Test Accuracy is {test_acc}')
        file_name = os.path.join(os.path.abspath("save"), "fashion_model.h5")
        print(f"저장경로: {file_name}")
        model.save(file_name)




iris_menu = ["Exit",  # 0
               "Learning",  # 1
               ]

iris_lambda = {
    "1": lambda x: x.create_model(),
    }

if __name__ == '__main__':
    fs = FruitsModel()
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