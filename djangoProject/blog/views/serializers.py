from rest_framework import serializers
from models import BlogView

class BlogViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogView
        fields = '__all__'
