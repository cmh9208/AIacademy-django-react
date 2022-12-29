from webcrawler.webcrawler_services import ScrapService


from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

scrap = ScrapService()
@api_view(['GET'])
@parser_classes([JSONParser])
def webcrawler(request):

    print(f'Enter show face with {request}')
    return JsonResponse({scrap.naver_movie_review()})