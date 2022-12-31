from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from shop.carts.repository import CartRepository
from shop.carts.serializers import CartSerializer


@api_view(['POST','PUT','PATCH','DELETE','GET'])
@parser_classes([JSONParser])
def cart(request):
    if request.method == "POST":
        return CartSerializer().create(request.data)
    elif request.method == "GET":
        return CartSerializer().find_by_id(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "PUT":
        return CartSerializer().update(request.data)
    elif request.method == "DELETE":
        return CartSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def cart_list(request): return CartRepository().get_all(request.data)


