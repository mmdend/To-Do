from rest_framework import serializers

from ...models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields = (
            "id",
            "title",
            "description",
            "snippet",
            "absolute_url",
            "is_completed",
            "created_at",
        )
        read_only_fields = ("id", "created_at")

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj)

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
