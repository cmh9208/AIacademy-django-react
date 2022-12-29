from django.urls import re_path as url

from ir import views

urlpatterns = [
    url(r'iris', views.iris)

]