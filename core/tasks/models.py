from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.description[0:10]

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Tasks"


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
