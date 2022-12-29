from rest_framework import serializers
from models import MovieTheater

class MovieTheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieTheater
        fields = '__all__'
