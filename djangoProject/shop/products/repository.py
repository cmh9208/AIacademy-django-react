from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


from shop.products.models import ShopProduct
from shop.products.serializers import ProductSerializer


class ProductRepository(object):

    def __init__(self):
        print(" Repository 객체 생성 ")

    def get_all(self):
        return Response(ProductSerializer(ShopProduct.objects.all(), many=True).data)

    def get_by_id(self):
        return Response(ProductSerializer(ShopProduct.objects.all(), many=True).data)



