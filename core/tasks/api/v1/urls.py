from django.urls import path, include

from . import views

app_name = 'api-v1'

urlpatterns = [
    # path('', views.tasks_list, name='tasks_list'),
    path('', views.TaskListCreateView.as_view(), name='task-list-create'),
]