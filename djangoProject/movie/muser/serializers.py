from rest_framework import serializers
from models import MovieMuser

class MovieMuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieMuser
        fields = '__all__'
