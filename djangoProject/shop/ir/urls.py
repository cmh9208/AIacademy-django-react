from django.urls import re_path as url

from shop.ir import views

urlpatterns = [
    url(r'iris', views.iris)

]