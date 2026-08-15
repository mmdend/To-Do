from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import Tasks
from .serializers import TaskSerializer

'''class TaskListCreateView(generics.ListCreateAPIView):
    """
    API view to list and create tasks for the current authenticated user.
    GET  /api/v1/tasks/  → list current user's tasks
    POST /api/v1/tasks/  → create a task
    """

    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ("title", "description")
    ordering_fields = ("created_at", "title")
    ordering = ("-created_at",)

    def get_queryset(self):
        # Users can only see their own tasks
        return Tasks.objects.filter(user=self.request.user)
'''


class TaskModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for managing tasks belonging to the currently authenticated user.
        GET    /api/v1/tasks/
        POST   /api/v1/tasks/
        GET    /api/v1/tasks/<id>/
        PUT    /api/v1/tasks/<id>/
        PATCH  /api/v1/tasks/<id>/
        DELETE /api/v1/tasks/<id>/
    """

    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # Users can only see their own tasks
        return Tasks.objects.filter(user=self.request.user)


'''class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET     /api/v1/tasks/<id>/  → retrieve a task
    PUT     /api/v1/tasks/<id>/  → full update
    PATCH   /api/v1/tasks/<id>/  → partial update
    DELETE  /api/v1/tasks/<id>/  → delete
    """

    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)
'''


class TaskCompleteView(APIView):
    """
    PATCH /api/v1/tasks/<id>/complete/  → mark task as complete
    """

    permission_classes = (IsAuthenticated,)

    def patch(self, request, pk):
        task = Tasks.objects.filter(pk=pk, user=request.user).first()
        if not task:
            return Response({"detail": "Not found."}, status=404)
        task.is_completed = True
        task.save()
        return Response(TaskSerializer(task, context={"request": request}).data)
