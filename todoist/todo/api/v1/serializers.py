from rest_framework import serializers

from todo.models import Task

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        read_only=True
    )

    title = serializers.CharField(
        required = True
    )

    content = serializers.CharField(
        required=False
    )

    done = serializers.BooleanField(
        required=True
    )

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.done = validated_data.get('done', instance.done)
        instance.save()
        return instance