from django.urls import re_path as url
from users import views

urlpatterns = [
    url(r'user$', views.comment),
    url(r'list$', views.user_list),
    url(r'list/name$', views.user_list_by_name), # 동명이인 있을 수 있어/name
    url(r'login', views.user_login),
]
