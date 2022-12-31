from rest_framework import serializers
from .models import ShopOrder as order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'

    def create(self, validated_data):
        return order.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        order.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass

    def find_by_id(self, data):
        pass
