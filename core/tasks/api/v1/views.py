from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from tasks.api.v1.filters import TaskFilter
from tasks.api.v1.paginations import DefaultPagination
from tasks.api.v1.permissions import IsOwner
from tasks.api.v1.serializers import CategorySerializer, TaskSerializer
from tasks.models import Category, Tasks


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
    permission_classes = (IsAuthenticated, IsOwner)

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )
    filterset_class = TaskFilter
    search_fields = ("title", "description")
    ordering_fields = ("title", "created_at", "updated_at")
    pagination_class = DefaultPagination

    def get_queryset(self):
        # Users can only see their own tasks
        return Tasks.objects.filter(user=self.request.user)


class CategoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


'''class TaskCompleteView(APIView):
    """
    PATCH /api/v1/tasks/<id>/complete/
    """

    permission_classes = (IsAuthenticated, IsOwner)

    def patch(self, request, pk):
        task = Tasks.objects.filter(pk=pk, user=request.user).first()
        if not task:
            return Response({"detail": "Not found."}, status=404)
        task.is_completed = True
        task.save()
        return Response(TaskSerializer(task, context={"request": request}).data)
'''

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
