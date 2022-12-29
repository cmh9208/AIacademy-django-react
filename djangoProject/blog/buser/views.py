from django.http import JsonResponse
from django.shortcuts import render
# from rest_framework.decorators import api_view, parser_classes
#
# from blog.buser.services import BuserService
#
# from rest_framework.parsers import JSONParser
# @api_view(['POST'])
# @parser_classes([JSONParser])
# def login(request):
#     user_info = request.data
#     email = user_info['email']
#     password = user_info['password']
#     print(f'리액트에서 보낸 데이터: {user_info}')
#     print(f'넘어온 이메일: {email}')
#     print(f'넘어온 비밀번호: {password}')
#     return JsonResponse({'로그인 결과' : '성공'})


from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from blog.buser.serializers import BlogBuserSerializer
from rest_framework.response import Response
from blog.buser.models import BlogBuser
from blog.buser.services import BuserService
from rest_framework.authtoken.models import Token
from users.models import User
from users.serializers import UserSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    try:
        print(f"로그인 정보: {request.data}")
        loginInfo = request.data
        loginUser = User.objects.get(user_email=loginInfo['user_email'])
        print(f"해당 email 을 가진  User ID: *** \n {loginUser.id}")
        if loginUser.password == loginInfo["password"]:
            dbUser = User.objects.all().filter(id=loginUser.id).values()[0]
            print(f" DBUser is {dbUser}")
            serializer = UserSerializer(dbUser, many=False)
            return JsonResponse(data=serializer.data, safe=False)
        # dictionary이외를 받을 경우, 두번째 argument를 safe=False로 설정해야한다.
        else:
            return print(" 비번이 틀립니다 ")
    except:
        return Response("LOGIN FAIL")










# @api_view(['POST'])
# def login(request):
#     return JsonResponse({'result ': BuserService().creat_busers()})

@api_view(['GET'])
@parser_classes([JSONParser])
def sign_up(request):
    return JsonResponse({'result ': BuserService().get_busers()})

# @api_view(['POST'])
# @parser_classes([JSONParser])
# def sign_up(request):
#     user_info = request.data
#     email = user_info['email']
#     password = user_info['password']
#     print(f'리액트에서 보낸 데이터: {user_info}')
#     print(f'넘어온 이메일: {email}')
#     print(f'넘어온 비밀번호: {password}')
#     return JsonResponse({'로그인 결과' : '성공'})