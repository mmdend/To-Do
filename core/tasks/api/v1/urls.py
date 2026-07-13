from django.urls import path

from . import views

app_name = 'api-v1'

urlpatterns = [
    # path('', views.tasks_list, name='tasks_list'),
    path('', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('<int:pk>/', views.TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('<int:pk>/complete/', views.TaskCompleteView.as_view(), name='task-complete'),
]