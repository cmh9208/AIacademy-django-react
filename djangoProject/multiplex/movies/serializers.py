from rest_framework import serializers
from .models import MultiplexMovie as movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = '__all__'

    def create(self, validated_data):
        return movie.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        movie.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
