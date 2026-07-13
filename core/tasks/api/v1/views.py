from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

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


class TaskCompleteView(APIView):
    """
    PATCH <id>/complete/  → mark task as complete
    """

    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        task = Tasks.objects.filter(pk=pk, user=request.user).first()
        if not task:
            return Response({"detail": "Not found."}, status=404)
        task.is_completed = True
        task.save()
        return Response(TaskSerializer(task, context={"request": request}).data)
