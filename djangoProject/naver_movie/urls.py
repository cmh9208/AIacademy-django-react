
from django.urls import re_path as url

from naver_movie import naver_view

urlpatterns = [
    url(r'naver', naver_view.naver_movie)

]