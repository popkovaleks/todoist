from django.urls import path

from todo.api.v1 import views

urlpatterns = [
    path('tasks', views.TaskViewset.as_view(
        {
            'get':'list',
            'post':'add'
        }
    ))
]