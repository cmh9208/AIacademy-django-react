from rest_framework import serializers
from models import ShopOrder

class ShopOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopOrder
        fields = '__all__'
