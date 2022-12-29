from rest_framework import serializers
from models import ShopDelivery

class ShopDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopDelivery
        fields = '__all__'
