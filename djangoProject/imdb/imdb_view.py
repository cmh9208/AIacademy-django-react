import json
from django.http import JsonResponse, QueryDict
from matplotlib import pyplot as plt
from rest_framework import serializers
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf
from imdb.imdb_service import NaverMovieService

# @api_view(['POST', 'GET'])
# @parser_classes([JSONParser])
# def imdb(request):
#     if request.method == 'POST':
#         id = json.loads(request.body)  # json to dict
#         print(f"######## POST id is {id} type is {type(id)} ########")
#         a = NaverMovieService().process(str(id))
#         print(f" 긍정일 확률 : {a} ")
#         return JsonResponse({'긍정일 확률': a})
#
#     elif request.method == 'GET':
#         print(f"######## GET id is {request.GET['id']} ########")
#         return JsonResponse(
#             {'긍정일 확률': NaverMovieService().process(str(request.GET['id']))})
#     else:
#         print(f"######## ID is None ########")

@api_view(['POST'])
@parser_classes([JSONParser])
def imdb(request):
    review = request.data
    print(f"******** 리액트에서 넘어온 리뷰 : {review} ******** ")
    result = NaverMovieService().process(review["inputs"])
    print(f'긍정률: {result}')

    return JsonResponse({'result': result})