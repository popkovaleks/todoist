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