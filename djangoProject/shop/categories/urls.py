from django.urls import re_path as url
from shop.categories import views

urlpatterns = [
    url(r'category', views.category),
    url(r'list', views.category_list)
]
