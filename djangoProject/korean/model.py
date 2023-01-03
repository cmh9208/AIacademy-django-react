import os
import pandas as pd
import tensorflow as tf
from keras import Sequential
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from tensorflow import keras
from keras.layers import Dense

import keras.datasets.imdb
import matplotlib.pyplot as plt
import numpy as np
from keras_preprocessing.sequence import pad_sequences
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

class KoreanClassifyModel(object):
    def __init__(self):
        pass

    # def hook(self)-> '':
    #     i = ['dd']
    #     ko_str = '이것은 한국어 문장입니다.'
    #     ja_str = 'これは日本語の文章です。'
    #     en_str = 'This is English Sentences.'
    #     x_train = [self.count_codePoint(ko_str),
    #                self.count_codePoint(ja_str),
    #                self.count_codePoint(en_str), ]
    #     y_train = ['ko', 'ja', 'en']
    #
    #
    #     ko_test_str = '안녕하세요'
    #     ja_test_str = 'こんにちは'
    #     en_test_str = 'Hello'
    #     clf = GaussianNB()
    #     clf.fit(x_train, y_train)
    #     x_test = [self.count_codePoint(ko_test_str),
    #                self.count_codePoint(ja_test_str),
    #                self.count_codePoint(en_test_str), ]
    #
    #     y_test = ['ko', 'ja', 'en']
    #     y_pred = clf.predict(x_test)
    #     print(y_pred)
    #     print(f'정답률: {accuracy_score(y_test, y_pred)}')

    # @staticmethod
    # def count_codePoint(str):
    #     counter = np.zeros(65535)
    #     for i in range(len(str)):
    #         code_point = ord(str[i])
    #         if code_point > 65535:
    #             continue
    #         counter[code_point] += 1
    #         counter = counter / len
    #     return counter

    import numpy as np

    def count_codePoint(self, str):

        counter = np.zeros(65535)

        for i in range(len(str)):
            code_point = ord(str[i])
            counter[code_point] += 1

        counter = counter / len(str)

        return counter

    def hook(self, i):
        ko_str = "이것은 한국어 문장입니다."
        en_str = "This is English Sentences."
        ja_str = "これは日本の文章です。"

        x_train = [self.count_codePoint(ko_str), self.count_codePoint(ja_str), self.count_codePoint(en_str)]
        print(x_train)
        y_train = ['ko', 'ja', 'en']

        from sklearn.naive_bayes import GaussianNB
        clf = GaussianNB()
        clf.fit(x_train, y_train)

        ko_test_str = '안녕하세요.'
        ja_test_str = 'こんにちは'
        en_test_str = 'Hello'
        # x_test = [self.count_codePoint(ko_test_str), self.count_codePoint(ja_test_str), self.count_codePoint(en_test_str)]
        x_test = [self.count_codePoint(i), self.count_codePoint(i), self.count_codePoint(i)]
        y_test = ['ko', 'ja', 'en']

        from sklearn.metrics import accuracy_score
        y_pred = clf.predict(x_test)
        a = y_pred[0]
        b = accuracy_score(y_test, y_pred) * 300
        print('정답률=', accuracy_score(y_test, y_pred)*100, '%')

        return ['감지된 언어=', a, '정답률=', b, "%"]

imdb_menu = ["Exit",  # 0
               "count_codePoint",  # 1
               ]

imdb_lambda = {
    "1": lambda x: x.hook(),
    }

if __name__ == '__main__':
    imdb = KoreanClassifyModel()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(imdb_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                imdb_lambda[menu](imdb)
            except:
                print("Didn't catch error message")