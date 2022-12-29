from rest_framework import serializers
from models import ShopCart

class ShopCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCart
        fields = '__all__'
