from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from shop.deliveries.repository import DeliveryRepository
from shop.deliveries.serializers import DeliverySerializer


@api_view(['POST','PUT','PATCH','DELETE','GET'])
@parser_classes([JSONParser])
def delivery(request):
    if request.method == "POST":
        return DeliverySerializer().create(request.data)
    elif request.method == "GET":
        return DeliverySerializer().find_by_id(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "PUT":
        return DeliverySerializer().update(request.data)
    elif request.method == "DELETE":
        return DeliverySerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def delivery_list(request): return DeliveryRepository().get_all(request.data)
