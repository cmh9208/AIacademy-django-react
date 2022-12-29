from rest_framework import serializers
from models import MovieShowtime

class MovieShowtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieShowtime
        fields = '__all__'
