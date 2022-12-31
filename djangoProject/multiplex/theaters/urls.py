from django.urls import re_path as url
from multiplex.theaters import views

urlpatterns = [
    url(r'theater', views.theater),
    url(r'list', views.theater_list)
]
