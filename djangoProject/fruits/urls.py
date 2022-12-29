
from django.urls import re_path as url

from fruits import fruits_view

urlpatterns = [
    url(r'fruits', fruits_view.fruits)
    # url(r'fashion/(?P<id>)$', fashion_view.fashion)

]