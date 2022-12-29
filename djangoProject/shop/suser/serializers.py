from rest_framework import serializers
from models import ShopSuser

class ShopSuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopSuser
        fields = '__all__'
