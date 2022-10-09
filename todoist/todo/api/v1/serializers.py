from rest_framework import serializers

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