from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from samsung_report.models import Controller
import json



from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes

from blog.buser.services import BuserService

from rest_framework.parsers import JSONParser
# @api_view(['GET'])
# @parser_classes([JSONParser])
# def nlp(request):
#     user_info = request.data
#     email = user_info['email']
#     password = user_info['password']
#     print(f'리액트에서 보낸 데이터: {user_info}')
#     print(f'넘어온 이메일: {email}')
#     print(f'넘어온 비밀번호: {password}')
#     return JsonResponse({Controller().data_analysis()})



@api_view(['GET'])
def nlp(request):
    return JsonResponse(
        {'result': Controller().data_analysis()})
# 최종적으로 불러오는 메소드에 리턴값이 있어야함



#
# @api_view(['POST'])
# def nlp(request):
#     return JsonResponse({'Response Test':Controller().data_analysis()})
