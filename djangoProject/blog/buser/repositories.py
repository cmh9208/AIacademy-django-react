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

class UserRepository(object):

    def a(self):
        pass

    def login(self, loginInfo):
        loginUser = User.objects.get(user_email=loginInfo['user_email'])  # 리액트에서 넘어온 데이터에서 유저메일을 추출(DB에서 일어나는 일)
        print(f"해당 email 을 가진  User ID: *** \n {loginUser.id}")
        if loginUser.password == loginInfo["password"]:
            dbUser = User.objects.all().filter(id=loginUser.id).values()[0]  # 쿼리를 던짐
            print(f" DBUser is {dbUser}")
            serializer = UserSerializer(dbUser, many=False)
            # 위의 코드는DB와 관련이 있어 models에서 작성하는 것이 편리함(ORM에서 DB는 항상 존재한다)
            # 위는 CQRS중 Q작업 코드
            return JsonResponse(data=serializer.data, safe=False)
        # dictionary이외를 받을 경우, 두번째 argument를 safe=False로 설정해야한다.
        else:
            # return JsonResponse({"data": "WRONG_PASSWORD"})
            return print(" 비번이 틀립니다 ")