from django.urls import path

from todo.api.v1 import views

urlpatterns = [
    path('tasks', views.TaskViewset.as_view(
        {
            'get':'list',
            'post':'add',
            'put':'update',
            'delete':'delete'
        }
    )),
    path('tasks/<int:pk>', views.TaskDetailViewset.as_view(
        {
            'get': 'details'
            }
    ))
]