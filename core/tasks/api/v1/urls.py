from rest_framework.routers import DefaultRouter

from . import views

app_name = "tasks-api"

router = DefaultRouter()
router.register("tasks", views.TaskModelViewSet, basename="tasks")
router.register("categories", views.CategoryModelViewSet, basename="categories")
urlpatterns = router.urls

# urlpatterns = [

#     path("tasks/", views.TaskListCreateView.as_view(), name="task-list-create"),
#     path(
#         "tasks/<int:pk>/",
#         views.TaskRetrieveUpdateDestroyView.as_view(),
#         name="task-detail",
#     ),
#     path(
#         "tasks/<int:pk>/complete/",
#         views.TaskCompleteView.as_view(),
#         name="task-complete",
#     ),
# ]
