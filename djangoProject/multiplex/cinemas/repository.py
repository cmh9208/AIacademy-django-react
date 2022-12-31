from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from multiplex.cinemas.models import MultiplexCinema
from multiplex.cinemas.serializers import CinemaSerializer


class CinemaRepository(object):

    def __init__(self):
        print(" CinemaRepository 객체 생성 ")

    def get_all(self):
        return Response(CinemaSerializer(MultiplexCinema.objects.all(), many=True).data)

    def get_by_id(self):
        return Response(CinemaSerializer(MultiplexCinema.objects.all(), many=True).data)

    def find_by_id(self, data):
        pass



