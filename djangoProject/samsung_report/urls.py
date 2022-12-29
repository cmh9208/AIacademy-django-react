from django.urls import re_path as url

from samsung_report import views as view_samsung_report

urlpatterns = [
    url(r'samsung', view_samsung_report.nlp)
]