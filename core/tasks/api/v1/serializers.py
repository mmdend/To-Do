from rest_framework import serializers

from ...models import Category, Tasks


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class TaskSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields = (
            "id",
            "user",
            "title",
            "description",
            "snippet",
            "absolute_url",
            "is_completed",
            "category",
            "created_at",
            "updated_date",
        )
        read_only_fields = ("id", "user", "created_at")

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get("request")
        # print(f"Request in serializer: {request.__dict__}")  # Debugging line
        if request.parser_context.get("kwargs").get("pk"):
            representation.pop("snippet", None)
            representation.pop("absolute_url", None)
        else:
            representation.pop("description", None)

        representation["category"] = (
            CategorySerializer(instance.category, context={"request": request}).data
            if instance.category
            else None
        )

        return representation

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
