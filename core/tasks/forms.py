from django import forms

from .models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["title", "description", "is_completed"]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Enter task title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "placeholder": "Enter description",
                    "rows": 4,
                }
            ),
            "is_completed": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }
