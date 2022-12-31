from rest_framework import serializers
from .models import ShopCart as cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = '__all__'

    def create(self, validated_data):
        return cart.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        cart.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass

    def find_by_id(self, data):
        pass
