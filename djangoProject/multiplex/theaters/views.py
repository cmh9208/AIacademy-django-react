from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from multiplex.theater_tickets.repository import TheaterTicketRepository
from multiplex.theater_tickets.serializers import TheaterTicketSerializer
from multiplex.theaters.serializers import TheaterSerializer


@api_view(['POST','PUT','PATCH','DELETE','GET'])
@parser_classes([JSONParser])
def theater(request):
    if request.method == "POST":
        return TheaterSerializer().create(request.data)
    elif request.method == "GET":
        return TheaterSerializer().find_by_id(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "PUT":
        return TheaterSerializer().update(request.data)
    elif request.method == "DELETE":
        return TheaterSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def theater_list(request): return TheaterTicketRepository().get_all(request.data)

