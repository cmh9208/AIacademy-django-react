from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from users.models import User
from users.services import UserService
from blog.buser import repositories

from users.repositories import UserRepository
from users.serializers import UserSerializer

@api_view(['POST', 'PUT', 'PATCH', 'DELETE', 'GET'])
@parser_classes([JSONParser])
def user(request):
    if request.method == "POST":
        new_user = request.data
        print(f" 리액트에서 등록한 신규 가입자 {new_user}")
        serializer = UserSerializer(data=new_user)
        if serializer.is_valid():
            serializer.save() # 외부에서 들어온 데이터 변형없이 저장
            return JsonResponse({"result":"SUCCESS"})  # return JsonResponse({'result ': BuserService().get_busers()})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 메일로 유저 찾기
    elif request.method == "GET":
        return Response(UserRepository()
                        .find_user_by_email(request.data["user_email"])) # dc로 들어오는 값에서 찾음

    elif request.method == "PATCH":
        return None
    # 전부 바꾸는것
    elif request.method == "PUT":
        repo = request.data
        modyfy_user = UserRepository().find_user_by_email(request.data["user_email"]) # 수정되는 유저
        db_user = repo.find_by_id(modyfy_user.id)
        serializer = UserSerializer(data=db_user)
        if serializer.is_valid():
            serializer.update(modyfy_user, db_user)
            return JsonResponse({"result": "SUCCESS"})

    elif request.method == "DELETE":
        repo = request.data
        delete_user = UserRepository().find_user_by_email(request.data["user_email"])  # 수정되는 유저
        db_user = repo.find_by_id(delete_user.id) # 삭제할땐 반드시 pk로 잡아야함
        db_user.delete()
        return JsonResponse({"result": "SUCCESS"})

@api_view(['POST'])
@parser_classes([JSONParser])
def user_login(request): return UserRepository().login(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def user_list(request): return UserRepository().get_all()

@api_view(['GET'])
@parser_classes([JSONParser])
def user_list_by_name(request):
    return UserRepository().user_list_by_name(request.data["user_email"]) # dc로 들어오는 값에서 찾음