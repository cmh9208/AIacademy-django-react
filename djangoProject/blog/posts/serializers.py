from rest_framework import serializers
from .models import BlogPost as post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = '__all__'

    def create(self, validated_data):
        return post.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        post.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
