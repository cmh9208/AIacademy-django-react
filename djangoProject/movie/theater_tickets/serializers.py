from rest_framework import serializers
from models import MovieTheaterTicket

class MovieTheaterTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieTheaterTicket
        fields = '__all__'
