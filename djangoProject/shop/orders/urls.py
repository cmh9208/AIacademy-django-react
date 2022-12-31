from django.urls import re_path as url
from shop.orders import views

urlpatterns = [
    url(r'order', views.order),
    url(r'list', views.order_list)
]
