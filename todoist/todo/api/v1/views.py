from rest_framework import viewsets, status
from rest_framework.response import Response

from todo.api.v1 import serializers
from todo import models

class TaskViewset(viewsets.ViewSet):

    def list(self, request):
        tasks = models.Task.objects.all()

        if tasks:
            return Response(data=serializers.TaskSerializer(tasks, many=True).data, status=status.HTTP_200_OK)
        return Response('No tasks found', status=status.HTTP_404_NOT_FOUND)


    def add(self, request):
        data = request.data
        serializer = serializers.TaskSerializer(data=data)

        if serializer.is_valid():
            models.Task.objects.create(
                title=serializer.data.get('title'),
                content=serializer.data.get('content'),
                done=serializer.data.get('done')
            )
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    
    def update(self, request):
        data = request.data
        serializer = serializers.TaskSerializer(data=data)

        if serializer.is_valid():
            models.Task.objects.get(id=serializer.data.get('id'))\
                .update(
                    title=serializer.data.get('title'),
                    content=serializer.data.get('content'),
                    done=serializer.data.get('done')
                )
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)