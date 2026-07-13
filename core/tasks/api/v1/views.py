from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import TaskSerializer
from ...models import Tasks


class TaskListCreateView(generics.ListCreateAPIView):
    """
    API view to list and create tasks for the current authenticated user.
    GET  /api/v1/  → list current user's tasks
    POST /api/v1/  → create a task
    """

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "title"]
    ordering = ["-created_at"]

    def get_queryset(self):
        # Users can only see their own tasks
        return Tasks.objects.filter(user=self.request.user)


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET     <id>/  → retrieve a task
    PUT     <id>/  → full update
    PATCH   <id>/  → partial update
    DELETE  <id>/  → delete
    """

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)
