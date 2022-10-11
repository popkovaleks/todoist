from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from todo.api.v1 import serializers
from todo import models

class TaskViewset(viewsets.ViewSet):

    def list(self, request):
        tasks = models.Task.objects.all().values('id','title','done')

        if tasks:
            return Response(data=serializers.TaskSerializer(tasks, many=True).data, status=status.HTTP_200_OK)
        return Response('No tasks found', status=status.HTTP_404_NOT_FOUND)


    def add(self, request):
        data = request.data
        serializer = serializers.TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    
    def update(self, request):
        data = request.data
        task = models.Task.objects.get(id=data.get('id'))
        serializer = serializers.TaskSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        data = request.data
        models.Task.objects.get(id=data.get('id')).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskDetailViewset(viewsets.ViewSet):

    def details(self, request, pk):
        task = models.Task.objects.get(id=pk)
        serializer = serializers.TaskSerializer(data=task.__dict__)

        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        