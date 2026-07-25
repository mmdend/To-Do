from django.urls import include, path

from . import views

app_name = "tasks"

urlpatterns = [
    path("tasks/", views.TaskListView.as_view(), name="list"),
    path("tasks/create/", views.TaskCreateView.as_view(), name="create"),
    path("tasks/update/<int:pk>/", views.TaskUpdateView.as_view(), name="update"),
    path("tasks/delete/<int:pk>/", views.TaskDeleteView.as_view(), name="delete"),
    path("api/v1/", include("tasks.api.v1.urls")),
]
