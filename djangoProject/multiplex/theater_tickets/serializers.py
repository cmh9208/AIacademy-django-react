from rest_framework import serializers
from .models import MultiplexTheaterTicket as theaterTicket


class TheaterTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = theaterTicket
        fields = '__all__'

    def create(self, validated_data):
        return theaterTicket.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        theaterTicket.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass

    def find_by_id(self, data):
        pass
