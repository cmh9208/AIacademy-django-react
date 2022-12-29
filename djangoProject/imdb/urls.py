
from django.urls import re_path as url

from imdb import imdb_view

urlpatterns = [
    url(r'imdb', imdb_view.imdb)
    # url(r'fashion/(?P<id>)$', fashion_view.fashion)

]