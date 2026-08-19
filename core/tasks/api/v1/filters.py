from django_filters import rest_framework as filters

from tasks.models import Category, Tasks


def user_categories(request):
    # Users can only see their own categories in the filter set
    if request is None or not request.user.is_authenticated:
        return Category.objects.none()

    return Category.objects.filter(user=request.user)


class TaskFilter(filters.FilterSet):
    """
    Filters tasks by category, completion status, and update date ranges.
    """

    category = filters.ModelChoiceFilter(
        queryset=user_categories,
    )
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
