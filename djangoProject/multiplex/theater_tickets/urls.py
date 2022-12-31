from django.urls import re_path as url
from multiplex.theater_tickets import views

urlpatterns = [
    url(r'theater-ticket', views.theater_ticket),
    url(r'list', views.theater_ticket_list)
]
