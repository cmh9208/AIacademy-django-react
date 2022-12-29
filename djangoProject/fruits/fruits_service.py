import numpy as np
import pandas as pd
import tensorflow as tf
from keras import Sequential
# from keras.applications.densenet import layers
from keras.layers import Dense
from keras.saving.save import load_model
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
import os

# from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt
import numpy as np


import tensorflow as tf
# import tensorflow_datasets as tfds
from keras.layers import Dense
from keras.layers import Conv2D

# from keras.callbacks import ModelCheckpoint
from tensorflow import keras
from keras.callbacks import ModelCheckpoint


class FruitsService(object):
    def __init__(self):
        global Train_Apple_Braeburn, Train_Apple_Crimson_Snow, Train_Apple_Golden1, Train_Apple_Golden2, Train_Apple_Golden3, \
            Test_Apple_Braeburn, Test_Apple_Crimson_Snow, Test_Apple_Golden1, Test_Apple_Golden2, Test_Apple_Golden3, train_data_dir, test_data_dir


        Train_Apple_Braeburn = r"C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\fruits\train\Apple Braeburn"
        Train_Apple_Crimson_Snow = r"C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\fruits\train\Apple Crimson Snow"
        Train_Apple_Golden1 = r"C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\fruits\train\Apple Golden 1"
        Train_Apple_Golden2 = r"C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\fruits\train\Apple Golden 2"
        Train_Apple_Golden3 = r"C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\fruits\train\Apple Golden 3"

        Test_Apple_Braeburn = r"C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\fruits\test\Apple Braeburn"
        Test_Apple_Crimson_Snow = r"C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\fruits\test\Apple Crimson Snow"
        Test_Apple_Golden1 = r"C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\fruits\test\Apple Golden 1"
        Test_Apple_Golden2 = r"C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\fruits\test\Apple Golden 2"
        Test_Apple_Golden3 = r"C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\fruits\test\Apple Golden 3"

        train_data_dir = r'C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\fruits\train'
        test_data_dir = r'C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\fruits\test'






    def show_apple(self):
        img = tf.keras.preprocessing.image.load_img(f"{Train_Apple_Golden3}//0_100.jpg")
        plt.imshow(img)
        plt.axis("off")
        plt.show()

        # 배치 사이즈를 32로 지정
        # 원 데이터 출처에서 제공된 정보에 기반하여 Image size를 100x100 pixels로 지정
        batch_size = 32
        img_height = 100
        img_width = 100

        # 원본 학습 데이터셋을 불러오기
        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            train_data_dir,
            validation_split=0.3,
            subset="training",
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size)

        # 원본 학습 데이터넷에서 검증 데이터셋을 분리
        val_ds = tf.keras.preprocessing.image_dataset_from_directory(
            train_data_dir,
            validation_split=0.3,
            subset="validation",
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size)

        # 불러온 학습 데이터엣에서 레이블 값(여기서는 5개 사과 품종)을 확인
        class_names = train_ds.class_names
        print(class_names)

        # 원본 테스트 데이터셋 불러오기
        test_ds = tf.keras.preprocessing.image_dataset_from_directory(
            test_data_dir,
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size)

        # 원본 테서트 데이터셋을 shuffle=False 옵션 추가하여 데이터셋 test_ds1을 별도로 생성
        test_ds1 = tf.keras.preprocessing.image_dataset_from_directory(
            test_data_dir,
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size,
            shuffle=False)

        type(test_ds)

        # test_ds에서 레이블 정보만 추출하여 y에 저장
        # 이 코딩문은 실행할 때마다 y 배열이 변경됨에 주의
        y = np.concatenate([y for x, y in test_ds], axis=0)
        print(y)

        # test_ds1에서 레이블 정보만 추출하여 y에 저장
        y = np.concatenate([y for x, y in test_ds1], axis=0)
        print(y)

        print(y[0])  # np.ndarray의 처음 항목을 출력
        print(y[-1])  # np.ndarray의 마지막 항목을 출력
        print(y[796])

        # test_ds1에서 이미지 정보만 추출하여 x에 저장

        x = np.concatenate([x for x, y in test_ds1], axis=0)
        print(x[0])

        # # test_ds1의 첫번째 이미지와 레이블을 불러와 그림으로 확인
        # plt.figure(figsize=(3, 3))
        # plt.imshow(x[0].astype("uint8"))
        # plt.title(class_names[y[0]])
        # plt.axis("off")
        # plt.show()
        #
        # # test_ds1의 마지막 이미지와 레이블을 불러와 그림으로 확인
        # plt.figure(figsize=(3, 3))
        # plt.imshow(x[-1].astype("uint8"))
        # plt.title(class_names[y[-1]])
        # plt.axis("off")
        # plt.show()

        # test_ds1을 제외하고 위에서 불러온 세가지 데이터셋을 Prefetch 데이터셋으로 설정
        BUFFER_SIZE = 10000
        AUTOTUNE = tf.data.experimental.AUTOTUNE

        train_ds = train_ds.cache().shuffle(BUFFER_SIZE).prefetch(buffer_size=AUTOTUNE)
        val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
        test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)
        type(train_ds)


        # 합성곱 신경망(CNN) 모델 구성
        num_classes = 5  # 레이블 값의 개수, 즉 사과 품종의 개수



        model = keras.Sequential([
            keras.layers.experimental.preprocessing.Rescaling(1. / 255, input_shape=(img_height, img_width, 3)),
            keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
            keras.layers.MaxPooling2D(2),
            keras.layers.Dropout(.50),
            keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
            keras.layers.MaxPooling2D(2),
            keras.layers.Dropout(.50),
            keras.layers.Flatten(),
            keras.layers.Dense(500, activation='relu'),
            keras.layers.Dropout(.50),
            keras.layers.Dense(num_classes, activation='softmax')
        ])

        # 모델을 컴파일
        model.compile(
            optimizer='adam',
            loss=tf.losses.SparseCategoricalCrossentropy(),
            metrics=['accuracy'])

        # 모델을 학습
        # 텐서플로 케라스 신경망 모델은 매번 실행시 모델 결과가 조금씩 다를 수 있음에 유의

        checkpointer = ModelCheckpoint('CNNClassifier.h5', save_best_only=True)
        early_stopping_cb = keras.callbacks.EarlyStopping(patience=5, monitor='val_accuracy',
                                                          restore_best_weights=True)
        epochs = 20

        history = model.fit(
            train_ds,
            batch_size=batch_size,
            validation_data=val_ds,
            epochs=epochs,
            callbacks=[checkpointer, early_stopping_cb]
        )

        # 참조 코딩
        len(history.history['val_accuracy'])

        # 매 epochs마다 모델 정확도와 손실을 그래프로 그리기

        acc = history.history['accuracy']  # 모델의 학습 정확도를 변수 acc에 저장
        val_acc = history.history['val_accuracy']  # 모델의 검증 정확도를 변수 val_acc에 저장

        loss = history.history['loss']  # 모델의 학습 손실을 변수 loss에 저장
        val_loss = history.history['val_loss']  # 모델의 검증 손실을 변수 val_loss에 저장

        # epochs가 14회가 아닌 다른 결과(예:10회)로 나오면 아래 줄 14를 해당 숫자인 10로 바꿔주야 함에 유의
        epochs_range = range(1, 14 + 1)  # epochs가 14회까지만 수행된 것을 반영

        # 학습 정확도와 검증 정확도를 그리기
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        # 학습 손실와 검증 손실을 그리기
        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')
        plt.show()

        # model.fit() 실행시 검증 정확도가 가장 높은 에포크에 해당하는 모델 가중치 계수들을 불러오기
        model.load_weights('CNNClassifier.h5')

        # 데이터셋 test_ds를 사용하여 모델을 평가

        test_loss, test_acc = model.evaluate(test_ds)

        print("test loss: ", test_loss)
        print()
        print("test accuracy: ", test_acc)

        # 특정 이미지의 레이블을 예측하기 위해서 test_ds1을 사용하여 예측을 실시
        # test_ds1의 첫번째 이미지의 예측 결과
        predictions = model.predict(test_ds1)
        score = tf.nn.softmax(predictions[0])

        print(
            "This image most likely belongs to {} with a {:.2f} percent confidence."
            .format(class_names[np.argmax(score)], 100 * np.max(score))
        )

        # test_ds1의 마지막 이미지의 예측 결과
        score = tf.nn.softmax(predictions[-1])

        print(
            "This image most likely belongs to {} with a {:.2f} percent confidence."
            .format(class_names[np.argmax(score)], 100 * np.max(score))
        )







iris_menu = ["Exit",  # 0
               "Learning",  # 1
               "lll",  # 2
               ]

iris_lambda = {
    "1": lambda x: x.show_apple(),
    "2": lambda x: x.lll(),
    }

if __name__ == '__main__':
    ir = FruitsService()
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


# import numpy as np
# import matplotlib.pyplot as plt
# from tensorflow import keras
# from keras.callbacks import ModelCheckpoint
# import tensorflow as tf
# import tensorflow_datasets as tfds
#
# class FruitsService:
#     def __init__(self):
#
#         global class_names, Apple_Braeburn_Test, Apple_Braeburn_Train, \
#             Apple_Crimson_Snow_Train, Apple_Golden_1_Train, Apple_Golden_2_Train, \
#             Apple_Golden_3_Train, Apple_Crimson_Snow_Test, Apple_Golden_1_Test, \
#             Apple_Golden_2_Test, Apple_Golden_3_Test, batch_size, img_height, img_width, \
#             trainpath, testpath
#
#         trainpath = r"C:\Users\AIA\PycharmProjects\djangoProject\fruits\train"
#         testpath = r"C:\Users\AIA\PycharmProjects\djangoProject\fruits\test"
#         Apple_Braeburn_Train = r"C:\Users\AIA\PycharmProjects\djangoProject\fruits\train\Apple Braeburn"
#         Apple_Crimson_Snow_Train = r"C:\Users\AIA\PycharmProjects\djangoProject\fruits\train\Apple Crimson Snow"
#         Apple_Golden_1_Train = r"C:\Users\AIA\PycharmProjects\djangoProject\fruits\test\Apple Golden 1"
#         Apple_Golden_2_Train = r"C:\Users\AIA\PycharmProjects\djangoProject\fruits\test\Apple Golden 2"
#         Apple_Golden_3_Train = r"C:\Users\AIA\PycharmProjects\djangoProject\fruits\test\Apple Golden 3"
#         Apple_Braeburn_Test = r"C:\Users\AIA\PycharmProjects\djangoProject\fruits\train\Apple Braeburn"
#         Apple_Crimson_Snow_Test = r"C:\Users\AIA\PycharmProjects\djangoProject\fruits\train\Apple Crimson Snow"
#         Apple_Golden_1_Test = r"C:\Users\AIA\PycharmProjects\djangoProject\fruits\test\Apple Golden 1"
#         Apple_Golden_2_Test = r"C:\Users\AIA\PycharmProjects\djangoProject\fruits\test\Apple Golden 2"
#         Apple_Golden_3_Test = r"C:\Users\AIA\PycharmProjects\djangoProject\fruits\test\Apple Golden 2"
#
#         batch_size = 32
#         img_height = 100
#         img_width = 100
#
#     def hook(self):
#         self.show_apple()
#         train_ds = self.create_train_ds()
#         validation_ds = self.create_validation_ds()
#         test_ds = self.create_test_ds()
#         print(f"*** Type of test_ds is {type(test_ds)} ***")
#         # Type of test_ds is tensorflow.python.data.ops.dataset_ops.BatchDataset
#         test_ds1 = self.create_test_ds1()
#         class_names = train_ds.class_names
#         self.merge_image_label_tester(test_ds=test_ds,
#                                test_ds1=test_ds1,
#                                class_names=class_names,
#                                index=-1) # -1 은 가장 마지막 인덱스
#
#
#     def show_apple(self):
#         img = tf.keras.preprocessing.image.load_img \
#             (f'{Apple_Golden_3_Train}\\0_100.jpg')
#         plt.imshow(img)
#         plt.axis("off")
#         plt.show()
#
#     def create_train_ds(self):
#         return tf.keras.preprocessing.image_dataset_from_directory(
#             trainpath,
#             validation_split=0.3,
#             subset="training",
#             seed=1,
#             image_size=(img_height, img_width),
#             batch_size=batch_size)
#
#     def create_validation_ds(self):
#         return tf.keras.preprocessing.image_dataset_from_directory(
#             trainpath,
#             validation_split=0.3,
#             subset="validation",
#             seed=1,
#             image_size=(img_height, img_width),
#             batch_size=batch_size)
#
#     def create_test_ds(self):
#         return tf.keras.preprocessing.image_dataset_from_directory(
#             testpath,
#             seed=1,
#             image_size=(img_height, img_width),
#             batch_size=batch_size)
#
#     def create_test_ds1(self):
#         return tf.keras.preprocessing.image_dataset_from_directory(
#             testpath,
#             seed=1,
#             image_size=(img_height, img_width),
#             batch_size=batch_size,
#             shuffle=False) # shuffle=False 데이터셋 test_ds1을 별도로 생성
#
#     def extract_label_from_ds(self, ds):
#         return np.concatenate([y for x, y in ds], axis=0)
#
#     def extract_image_info(self, ds):
#         return np.concatenate([x for x, y in ds], axis=0)
#
#     def merge_image_label_tester(self, **kwargs):
#         test_ds = kwargs["test_ds"]
#         test_ds1 = kwargs["test_ds1"]
#         class_names = kwargs["class_names"]
#         y = self.extract_label_from_ds(test_ds)
#         print(f"test_ds에서 레이블 정보만 추출하여 y에 저장\n"
#               f"실행할 때마다 y 배열이 변경됨: {y}\n")
#         y = self.extract_label_from_ds(test_ds1)
#         print(f"Shuffle=False 옵션을 통해 불러온 test_ds1 정보를 y에 저장\n"
#               f"실행할 때마다 y 배열이 변경이 없음: {y}\n")
#         x = self.extract_image_info(kwargs["test_ds1"])
#         print(f"test_ds1에서 이미지 정보만 추출하여 x에 저장 : {x[0]}\n")
#         plt.figure(figsize=(3, 3))
#         plt.imshow(x[0].astype("uint8"))
#         plt.title(class_names[y[0]])
#         plt.axis("off")
#         plt.show()
#
#     def merge_image_label(self, **kwargs):
#         dataset = kwargs["dataset"]
#         class_names = kwargs["class_names"]
#         i = kwargs["index"]
#         x = self.extract_image_info(dataset)
#         y = self.extract_label_from_ds(dataset)
#         plt.figure(figsize=(3, 3))
#         plt.imshow(x[i].astype("uint8"))
#         plt.title(class_names[y[i]])
#         plt.axis("off")
#         plt.show()
#
# if __name__ == '__main__':
#     FruitsService().hook()