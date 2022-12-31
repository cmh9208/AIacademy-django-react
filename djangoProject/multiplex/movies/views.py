from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from multiplex.movies.repository import MovieRepository
from multiplex.movies.serializers import MovieSerializer


@api_view(['POST','PUT','PATCH','DELETE','GET'])
@parser_classes([JSONParser])
def movies(request):
    if request.method == "POST":
        return MovieSerializer().create(request.data)
    elif request.method == "GET":
        return MovieRepository().find_by_id(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "PUT":
        return MovieSerializer().update(request.data)
    elif request.method == "DELETE":
        return MovieSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def movies_list(request): return MovieRepository().get_all(request.data)




