"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from admin.views import hello

urlpatterns = [

    path('', hello),
    path("blog/auth/", include('blog.buser.urls')),
    path("mplex/movies/", include('movie.movies.urls')),
    path("blog/st/", include('blog.st.urls')),
    path("shop/ir/", include('shop.ir.urls')),
    path("fashion/", include('fashion.urls')),
    path("number/", include('number.urls')),
    path("webcrawler/", include('webcrawler.urls')),
    path("fruits/", include('fruits.urls')),
    path("samsung_report/", include('samsung_report.urls')),
    path("naver_movie/", include('naver_movie.urls')),
    path("users/", include('users.urls')),
    path("imdb/", include('imdb.urls')),



]

