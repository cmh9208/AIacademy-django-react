from django.urls import re_path as url
from shop.products import views

urlpatterns = [
    url(r'product', views.product),
    url(r'list', views.product_list)
]
