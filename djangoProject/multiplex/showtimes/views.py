from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from multiplex.showtimes.repository import ShowtimeRepository
from multiplex.showtimes.serializers import ShowtimeSerializer


@api_view(['POST','PUT','PATCH','DELETE','GET'])
@parser_classes([JSONParser])
def showtime(request):
    if request.method == "POST":
        return ShowtimeSerializer().create(request.data)
    elif request.method == "GET":
        return ShowtimeSerializer().find_by_id(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "PUT":
        return ShowtimeSerializer().update(request.data)
    elif request.method == "DELETE":
        return ShowtimeSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def showtime_list(request): return ShowtimeRepository().get_all(request.data)
