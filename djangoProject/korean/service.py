import numpy as np
import pandas as pd
import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from keras.saving.save import load_model
from matplotlib import pyplot as plt

# from sentence_transformers.models import tokenizer

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OneHotEncoder
import os
import csv
import os.path

import pandas as pd
from selenium import webdriver

from webcrawler.models import ScrapVO
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tensorflow import keras
from keras_preprocessing.sequence import pad_sequences
import csv
import time
from os import path
from collections import defaultdict
from math import log, exp
root = r"C:\Users\최민호\PycharmProjects\AIacademy-django-react\djangoProject"

class ImdbService(object):
    def __init__(self):
        pass




    @staticmethod
    def count_codePoint(str):
        counter = np.zeros(65535)
        for i in range(len(str)):
            code_point = ord(str[i])
            if code_point > 65535:
                continue
            counter[code_point] += 1
            counter = counter / len


    def imdb_service_model(self) -> '':

        model = load_model(os.path.join(root, "imdb", "save", "best-rstm-model.h5"))
        (train_input, train_target), (test_input, test_target) = keras.datasets.imdb.load_data(num_words=500)
        test_seq = pad_sequences(test_input, maxlen=100) # test_input을 임베딩 방식 fit에 쓰인 train_input과 같이 만들어줌
        predictions = model.predict(test_seq)

        i = 53
        result = predictions[i]
        print(f'{result * 100} 확률로 긍정 리뷰 입니다.')

        # j = 0
        # for i in range(20):
        #     result = predictions[j]
        #     print(f'{j}번 리뷰는')
        #     j += 1
        #     if result > 0.5:
        #         print(f'{result * 100} 확률로 긍정 리뷰 입니다.')
        #     else:
        #         print(f'{(1 - result) * 100} 확률로 부정 리뷰 입니다.')


class NaverMovieService(object):
    def __init__(self):
        global url, driver, file_name, encoding, review_train, k, dr
        url = 'https://movie.naver.com/movie/point/af/list.naver?&page='
        dr = os.path.join(root, "imdb", "data", "chromedriver.exe")
        file_name = os.path.join(root, "imdb", "save", "naver_movie_review_corpus.csv")
        review_train = os.path.join(root, "imdb", "data", "review_train.csv")
        encoding = "UTF-8"
        self.word_probs = []
        k=0.5

    def process(selfm, new_review) -> float:
        service = NaverMovieService()
        service.model_fit()
        result = service.classify(new_review)
        # return round(result * 100, 1)
        return result

    def crawling(self):
        if not path.exists(file_name):
            review_data = []
            driver = webdriver.Chrome(dr)
            for page in range(1, 2):
                driver.get(url + str(page))
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                all_tds = soup.find_all('td', attrs={'class', 'title'})
                for review in all_tds:
                    need_reviews_cnt = 1000
                    sentence = review.find("a", {"class": "report"}).get("onclick").split("', '")[2]
                    if sentence != "":  # 리뷰 내용이 비어있다면 데이터를 사용하지 않음
                        score = review.find("em").get_text()
                        review_data.append([sentence, int(score)])
            time.sleep(1)  # 다음 페이지를 조회하기 전 1초 시간 차를 두기
            with open(file_name, 'w', newline='', encoding=encoding) as f:
                wr = csv.writer(f)
                wr.writerows(review_data)
            driver.close()

        data = pd.read_csv(file_name, header=None)
        data.columns = ['review', 'score']
        result = [print(f"{i + 1}. {data['score'][i]}\n{data['review'][i]}\n") for i in range(len(data))]
        return result

    def load_corpus(self):
        corpus = pd.read_table(review_train,sep=",", encoding=encoding)
        corpus = np.array(corpus)
        return corpus

    def count_words(self, train_X):
        counts = defaultdict(lambda : [0,0])
        for doc, point in train_X:
            if self.isNumber(doc) is False:
                words = doc.split()
                for word in words:
                    counts[word][0 if point > 3.5 else 1] += 1
        return counts

    def isNumber(self, param):
        try:
            float(param)
            return True
        except ValueError:
            return False

    def probability(self, word_probs, doc):
        docwords = doc.split()
        log_prob_if_class0 = log_prob_if_class1 = 0.0
        for word, prob_if_class0, prob_if_class1 in word_probs:
            if word in docwords:
                log_prob_if_class0 += log(prob_if_class0)
                log_prob_if_class1 += log(prob_if_class1)
            else:
                log_prob_if_class0 += log(1.0 - prob_if_class0)
                log_prob_if_class1 += log(1.0 - prob_if_class1)
        prob_if_class0 = exp(log_prob_if_class0)
        prob_if_class1 = exp(log_prob_if_class1)
        return prob_if_class0 / (prob_if_class0 + prob_if_class1)

    def word_probablities(self, counts, n_class0, n_class1, k):
        return [(w,
                 (class0 + k) / (n_class0 + 2 * k),
                 (class1 + k) / (n_class1 + 2 * k))
                for w, (class0, class1) in counts.items()]

    def classify(self, doc):
        return self.probability(word_probs=self.word_probs, doc=doc)

    def model_fit(self):
        train_X = self.load_corpus()
        '''
        '재밌네요': [1,0]
        '별로 재미없어요': [0,1]
        '''
        num_class0 = len([1 for _, point in train_X if point > 3.5])
        num_class1 = len(train_X) - num_class0
        word_counts = self.count_words(train_X)
        # print(f" ************  word_counts is {word_counts}")
        self.word_probs = self.word_probablities(word_counts, num_class0, num_class1, k)

# if __name__ == '__main__':
#     # ImdbService().hook()
#     result = NaverMovieService().process("진짜 쓰레기같은 영화다 개 재미없다")
#     print(f'{result * 100} 확률로 긍정 리뷰 입니다.')

imdb_menu = ["Exit",  # 0
               "imdb",  # 1
               ]

imdb_lambda = {
    "1": lambda x: x.imdb_service_model(),
    }

if __name__ == '__main__':
    imdb = ImdbService()
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