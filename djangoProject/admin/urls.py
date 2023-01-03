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
    # path("blog/buser/", include('blog.buser.urls')),
    path("st/", include('st.urls')),
    path("ir/", include('ir.urls')),
    path("fashion/", include('fashion.urls')),
    path("number/", include('number.urls')),
    path("webcrawler/", include('webcrawler.urls')),
    path("fruits/", include('fruits.urls')),
    # path("samsung_report/", include('samsung_report.urls')),
    path("naver_movie/", include('naver_movie.urls')),
    path("users/", include('users.urls')),
    path("imdb/", include('imdb.urls')),
    path("korean/", include('korean.urls')),
    path("aitrader/", include('aitrader.urls')),

    path("blog/comments/", include('blog.comments.urls')),
    path("blog/posts/", include('blog.posts.urls')),
    path("blog/tags/", include('blog.tags.urls')),
    path("blog/views/", include('blog.views.urls')),

    path("multiplex/cinemas/", include('multiplex.cinemas.urls')),
    path("multiplex/movies/", include('multiplex.movies.urls')),
    path("multiplex/showtimes/", include('multiplex.showtimes.urls')),
    path("multiplex/theater_tickets/", include('multiplex.theater_tickets.urls')),
    path("multiplex/theaters/", include('multiplex.theaters.urls')),

    path("shop/carts/", include('multiplex.movies.urls')),
    path("shop/categories/", include('shop.categories.urls')),
    path("shop/deliveries/", include('shop.deliveries.urls')),
    path("shop/orders/", include('shop.orders.urls')),
    path("shop/products/", include('shop.products.urls')),



]

