from django.urls import re_path as url
from blog.st import views

urlpatterns = [
    url(r'stroke', views.stroke)
]
