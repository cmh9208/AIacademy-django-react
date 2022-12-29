from django.urls import re_path as url, path

from admin.views import hello
from blog.buser import views

urlpatterns = [
    url(r'login',views.login),
    url(r'signup', views.sign_up)
]
