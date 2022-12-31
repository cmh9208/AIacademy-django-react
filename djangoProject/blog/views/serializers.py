from rest_framework import serializers
from .models import BlogView as view


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = view
        fields = '__all__'

    def create(self, validated_data):
        return view.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        view.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
