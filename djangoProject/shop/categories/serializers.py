from rest_framework import serializers
from .models import ShopCategory as category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

    def create(self, validated_data):
        return category.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        category.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass

    def find_by_id(self, data):
        pass
