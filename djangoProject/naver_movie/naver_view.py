import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from naver_movie.services import ScrapService


@api_view(['GET'])
@parser_classes([JSONParser])
def naver_movie(request):
    return JsonResponse(
        {'result': ScrapService().naver_movie_review()})


