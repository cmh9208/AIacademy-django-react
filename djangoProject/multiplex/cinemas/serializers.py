from rest_framework import serializers
from .models import MultiplexCinema as cinema


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = cinema
        fields = '__all__'

    def create(self, validated_data):
        return cinema.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        cinema.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
