from rest_framework import serializers
from .models import BlogComment as comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'

    def create(self, validated_data):
        return comment.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        comment.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
