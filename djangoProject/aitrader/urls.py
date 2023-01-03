
from django.urls import re_path as url

from aitrader import view

urlpatterns = [
    url(r'aitrader', view.aitrader),
    # url(r'fashion/(?P<id>)$', fashion_view.fashion)

]