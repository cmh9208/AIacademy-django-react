from django.urls import re_path as url
from multiplex.showtimes import views

urlpatterns = [
    url(r'showtime', views.showtime),
    url(r'list', views.showtime_list)
]
