from rest_framework import serializers
from models import ShopProduct

class ShopProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopProduct
        fields = '__all__'
