from rest_framework import serializers
from .models import ShopDelivery as delivery


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = delivery
        fields = '__all__'

    def create(self, validated_data):
        return delivery.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        delivery.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass

    def find_by_id(self, data):
        pass
