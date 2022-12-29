from rest_framework import serializers
from .models import BlogBuser

class BlogBuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogBuser
        fields = '__all__'
