from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-input"}))

    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}))

    avatar = forms.ImageField(
        required=False, widget=forms.ClearableFileInput(attrs={"class": "form-input"})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-input"})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-input"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "avatar", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-input", "placeholder": "Username"})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Password"}
        )
    )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "avatar"]

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-input"}),
            "email": forms.EmailInput(attrs={"class": "form-input"}),
            "avatar": forms.ClearableFileInput(attrs={"class": "form-input"}),
        }
