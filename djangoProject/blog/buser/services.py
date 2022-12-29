import random
import string
import pandas as pd
from sqlalchemy import create_engine
class BuserService(object):
    def __init__(self):
        pass
    def create_users(self):
        df = self.frame_create()
        engine = create_engine(
            "mysql+pymysql://root:root@localhost:3306/mydb",
            encoding='utf-8')
        df.to_sql(name='blog_busers',
                  if_exists='append',
                  con = engine,
                  index=False)
    def frame_create(self):
        n = 5
        email = ''
        golbang = '@google.com'
        password = 1
        nickname = 'NICK'
        data = []
        #email_list = list()
        for i in range(100):
            for i in range(n):
                email +=str(random.choice(string.ascii_letters))
            email += golbang
            data.append([email,nickname,password])
            email = ''
        df = pd.DataFrame(data,columns=['email','nickname','password'])
        #중복체크
        #df2 = pd.DataFrame([[1],[2],[1]] ,columns=['email'])
        #print(df2)
        #print(df2.duplicated(['email']))
        print(df.duplicated(['email']))
        return df
if __name__ == '__main__':
    s =BuserService()
    s.create_users() # 만듬 이미 돌리지마


#
#
# import string
# import random
# from random import shuffle
# import pandas as pd
# from sqlalchemy import create_engine
#
# from algorithms.lambdas import lambda_string, lambda_k_name, lambda_number, random_number, lambda_phone, \
#     lambda_birth, address_list, job_list, interests_list
#
#
# class UserService(object):
#     def __init__(self):
#         global engine
#         engine = create_engine(
#             "mysql+pymysql://root:root@localhost:3306/mydb",
#             encoding='utf-8')
#
#     def insert_users(self):
#         df = self.create_users()
#         df.to_sql(name='users',
#                   if_exists='append',
#                   con=engine,
#                   index=False)
#
#     '''
#      model의 dtype이 숫자인 AutoField로 돼있어서 임시로 수정되면
#      "blog_userid= ''.join(random.sample(string_pool, 5))"로 변경
#      (email도 email = blog_userid + "@naver.com"로 변경)
#     '''
#     def create_user(self)->[]:
#         user_email = str(lambda_string(4)) + "@test.com"
#         password = '1'
#         user_name = lambda_k_name(2)
#         phone = lambda_phone(4)
#         birth = lambda_birth(1985, 2011)
#         address = random.choice(address_list)
#         job = random.choice(job_list)
#         user_interests = random.choice(interests_list)
#         token = 'JWT fefege..'
#         '''
#         user_email = models.TextField()
#         password = models.CharField(max_length=10)
#         user_name = models.TextField()
#         phone = models.TextField()
#         birth = models.TextField()
#         address = models.TextField(blank=True)
#         job = models.TextField()
#         user_interests = models.TextField()
#         '''
#         return [user_email, password, user_name, phone, birth,
#                 address, job, user_interests, token]
#
#
#     def create_users(self)->[]:
#         rows = [self.create_user() for i in range(100)]
#         columns = ['user_email', 'password', 'user_name', 'phone', 'birth', 'address', 'job', 'user_interests', 'token']
#         df = pd.DataFrame(rows, columns=columns)
#         df['user_email'] = df['user_email'].astype(str)
#         return df
#
#     def get_users(self)->[]:
#         print(" 포스트맨의 요청이 도달하였음 !!")
#
#     def userid_checker(self):  # 아이디 중복체크
#         pass
#         '''print('중복 확인')
#         df = self.create_users()
#         if df.duplicated(['blog_userid'], keep=False) == True:
#             print('중복된 아이디입니다')
#         else:
#             return df'''
#
#
# if __name__ == '__main__':
#     UserService().insert_users()