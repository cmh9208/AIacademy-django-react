import pandas as pd
import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder

class Iris(object):
    def __init__(self):
        # self.iris = pd.read_csv(r'C:\Users\AIA\PycharmProjects\djangoProject\shop\ir\data\Iris.csv')
        self.iris = datasets.load_iris()
        print(f'type {type(self.iris)}')
        self._X = self.iris.data
        self._Y = self.iris.target

    ######## 분류 ########
    def create_model(self):
        X = self._X
        Y = self._Y
        enc = OneHotEncoder()
        Y_1hot = enc.fit_transform(Y.reshape(-1, 1)).toarray()
        model = Sequential()
        model.add(Dense(4, input_dim=4, activation='relu')) #피쳐4개
        model.add(Dense(3, activation='softmax')) #타깃3개
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        # my
        model.fit(X, Y_1hot, epochs=300, batch_size=10)
        print('Model Training is completed')

        file_name = './save/iris_model.h5'
        model.save(file_name)
        print(f'Model Saved in {file_name}')

    def hook(self):
        # self.spec()
        self.create_model()

    def spec(self):
        iris = self.iris
        print(iris.keys())
        # print(" --- 1.Shape ---")
        # print(iris.shape)
        # print(" --- 2.Features ---")
        # print(iris.columns)
        # print(" --- 3.Info ---")
        # print(iris.info())
        # print(" --- 4.Case Top1 ---")
        # print(iris.head(1))
        # print(" --- 5.Case Bottom1 ---")
        # print(iris.tail(3))
        # print(" --- 6.Describe ---")
        # print(iris.describe())
        # print(" --- 7.Describe All ---")
        # print(iris.describe(include='all'))

        '''
        Shape (150, 6)
        'Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 
        'PetalWidthCm', 'Species'
        '''

iris_menu = ["Exit",  # 0
               "Learning",  # 1
               ]

iris_lambda = {
    "1": lambda x: x.hook(),
    }

if __name__ == '__main__':
    Iris = Iris()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(iris_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                iris_lambda[menu](Iris)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")