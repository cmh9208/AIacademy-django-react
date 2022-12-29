from django.urls import re_path as url

from movie.movies import views

urlpatterns = [
    url(r'fake-faces', views.fake_faces)

]