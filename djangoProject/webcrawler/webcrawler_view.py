import json

from django.http import JsonResponse, QueryDict
from matplotlib import pyplot as plt
from rest_framework import serializers
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from webcrawler.models import ScrapVO
from webcrawler.webcrawler_services import ScrapService


from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from blog.st.stroke import Stroke

scrap = ScrapService()
@api_view(['GET'])
@parser_classes([JSONParser])
def webcrawler(request):

    print(f'Enter show face with {request}')
    return JsonResponse({scrap.naver_movie_review()})