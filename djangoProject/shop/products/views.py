from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from shop.products.repository import ProductRepository
from shop.products.serializers import ProductSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def create_product(request): return ProductSerializer().create(request.data)

@api_view(['POST','PUT','PATCH','DELETE','GET'])
@parser_classes([JSONParser])
def product(request):
    if request.method == "POST":
        return ProductSerializer().create(request.data)
    elif request.method == "GET":
        return ProductSerializer().find_by_id(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "PUT":
        return ProductSerializer().update(request.data)
    elif request.method == "DELETE":
        return ProductSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def product_list(request): return ProductRepository().get_all(request.data)
