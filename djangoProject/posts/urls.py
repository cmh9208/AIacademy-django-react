from django.urls import re_path as url
from blog.posts import views

urlpatterns = [
    url(r'posts', views.posts)
]
