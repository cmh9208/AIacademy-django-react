
from django.urls import re_path as url

from number import number_view

urlpatterns = [
    url(r'number', number_view.number)
    # url(r'fashion/(?P<id>)$', fashion_view.fashion)

]