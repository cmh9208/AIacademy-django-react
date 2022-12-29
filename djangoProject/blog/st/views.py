from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from blog.st.stroke import Stroke


@api_view(['GET'])
@parser_classes([JSONParser])
def stroke(request):
    Stroke().hook()
    print(f'Enter show face with {request}')
    return JsonResponse({'Response Test' : 'SUCCESS'})