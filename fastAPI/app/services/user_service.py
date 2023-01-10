from app.models.user import User


class UserService:
    def login(self, user_email, password):
        user = User(user_email, password)
        print(f" 리액트에서 보낸 이메일: {user.get_email()}")
        print(f" 리액트에서 보낸 이메일: {user.get_password()}")

#     def login(self, kwargs):
#         loginUser = User.objects.get(user_email=kwargs['user_email'])  # 리액트에서 넘어온 데이터에서 유저메일을 추출(DB에서 일어나는 일)
#         if loginUser.password == kwargs["password"]:
#             dbUser = self.find_by_id(loginUser.id)  # 쿼리를 던짐
#             serializer = UserSerializer(dbUser, many=False)
#             # 위의 코드는DB와 관련이 있어 models에서 작성하는 것이 편리함(ORM에서 DB는 항상 존재한다)
#             # 위는 CQRS중 Q작업 코드
#             return {serializer.data}
#         # dictionary이외를 받을 경우, 두번째 argument를 safe=False로 설정해야한다.
#         else:
#             return {"data": "WRONG_PASSWORD"}
#     def find_by_id(self, id):
#         return User.objects.all().filter(id=id).values()[0]
#
#
#
# from rest_framework import serializers
#
# class UserSerializer(serializers.ModelSerializer):
#     user_email = serializers.CharField()
#     password = serializers.CharField()
#     user_name = serializers.CharField()
#     phone = serializers.CharField()
#     birth = serializers.CharField()
#     address = serializers.CharField()
#     job = serializers.CharField()
#     user_interests = serializers.CharField()
#     token = serializers.CharField()
