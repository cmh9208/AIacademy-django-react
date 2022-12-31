from rest_framework import serializers
from .models import MultiplexTheater as theater


class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = theater
        fields = '__all__'

    def create(self, validated_data):
        return theater.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        theater.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass

    def find_by_id(self, data):
        pass
