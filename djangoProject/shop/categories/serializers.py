from rest_framework import serializers
from models import ShopCategory

class ShopCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCategory
        fields = '__all__'
