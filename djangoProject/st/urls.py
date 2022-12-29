from django.urls import re_path as url
from st import views

urlpatterns = [
    url(r'stroke', views.stroke)
]
