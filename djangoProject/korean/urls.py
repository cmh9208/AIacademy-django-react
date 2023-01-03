
from django.urls import re_path as url

from korean import view

urlpatterns = [
    url(r'korean', view.korean)
    # url(r'fashion/(?P<id>)$', fashion_view.fashion)

]