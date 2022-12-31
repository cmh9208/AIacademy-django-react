from django.urls import re_path as url
from multiplex.cinemas import views

urlpatterns = [
    url(r'cinema', views.cinema),
    url(r'list', views.cinema_list)
]
