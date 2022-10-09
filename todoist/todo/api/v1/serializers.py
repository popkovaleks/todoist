from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(
        required = True
    )

    content = serializers.CharField(
        required=False
    )

    done = serializers.BooleanField(
        required=True,
        default=False
    )