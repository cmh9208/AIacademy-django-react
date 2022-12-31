from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


from shop.carts.models import ShopCart
from shop.carts.serializers import CartSerializer


class CartRepository(object):

    def __init__(self):
        print(" CommentsRepository 객체 생성 ")

    def get_all(self):
        return Response(CartSerializer(ShopCart.objects.all(), many=True).data)

    def get_by_id(self):
        return Response(CartSerializer(ShopCart.objects.all(), many=True).data)



