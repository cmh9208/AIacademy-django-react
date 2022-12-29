
from django.urls import re_path as url

from number import number_view
from webcrawler import webcrawler_view

urlpatterns = [
    url(r'webcrawler', webcrawler_view.webcrawler)
    # url(r'fashion/(?P<id>)$', fashion_view.fashion)

]