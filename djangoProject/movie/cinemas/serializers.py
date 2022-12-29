from rest_framework import serializers
from models import MovieCinema

class MovieCinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCinema
        fields = '__all__'
