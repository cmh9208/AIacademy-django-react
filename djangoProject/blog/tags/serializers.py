from rest_framework import serializers
from .models import BlogTag as tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = '__all__'

    def create(self, validated_data):
        return tag.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        tag.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
