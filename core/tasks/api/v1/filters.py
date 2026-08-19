from django_filters import rest_framework as filters

from tasks.models import Tasks


class TaskFilter(filters.FilterSet):
    """
    Filters tasks by category, completion status, and update date ranges.
    """

    updated_at_after = filters.DateTimeFilter(
        field_name="updated_at",
        lookup_expr="gte",
    )
    updated_at_before = filters.DateTimeFilter(
        field_name="updated_at",
        lookup_expr="lte",
    )

    class Meta:
        model = Tasks
        fields = [
            "category",
            "is_completed",
        ]
