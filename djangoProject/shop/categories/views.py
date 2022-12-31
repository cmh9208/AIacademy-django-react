from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from shop.categories.repository import CategoryRepository
from shop.categories.serializers import CategorySerializer


@api_view(['POST','PUT','PATCH','DELETE','GET'])
@parser_classes([JSONParser])
def category(request):
    if request.method == "POST":
        return CategorySerializer().create(request.data)
    elif request.method == "GET":
        return CategorySerializer().find_by_id(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "PUT":
        return CategorySerializer().update(request.data)
    elif request.method == "DELETE":
        return CategorySerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def category_list(request): return CategoryRepository().get_all(request.data)
