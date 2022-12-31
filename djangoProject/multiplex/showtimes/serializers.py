from rest_framework import serializers
from .models import MultiplexShowtime as showtime


class ShowtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = showtime
        fields = '__all__'

    def create(self, validated_data):
        return showtime.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        showtime.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
