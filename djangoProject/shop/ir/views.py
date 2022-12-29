from django.http import JsonResponse, QueryDict
from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf
from shop.ir.iris import Iris
from shop.ir.iris_service import IrisService


@api_view(['POST'])
@parser_classes([JSONParser])
def iris(request):
    iris_data = request.data
    petal_width = tf.constant(float(iris_data['petal_width']))
    petal_length = tf.constant(float(iris_data['petal_length']))
    sepal_width = tf.constant(float(iris_data['sepal_width']))
    sepal_length = tf.constant(float(iris_data['sepal_length']))

    result = IrisService().service_model([petal_width, petal_length, sepal_width, sepal_length])


    print(f'리액트에서 보낸 데이터: {iris_data}')

    print(f'넘어온 꽃잎 폭: {petal_width}')
    print(f'넘어온 꽃잎 길이: {petal_length}')
    print(f'넘어온 꽃받침 폭: {sepal_width}')
    print(f'넘어온 꽃받침 길이: {sepal_length}')
    print(f'Enter show face with {request}')
    print(f'찾는 품종: {result}')

    if result == 0:
        resp = 'setosa / 부채붓꽃'
    elif result == 1:
        resp = 'versicolor / 버시칼라 '
    elif result == 2:
        resp = 'virginica / 버지니카'

    return JsonResponse({'resp' : resp})
