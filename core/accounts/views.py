from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from django.views.generic.edit import CreateView

from .forms import LoginForm, ProfileUpdateForm, RegisterForm

User = get_user_model()


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "accounts/register_page.html"
    success_url = reverse_lazy("accounts:profile")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()

        login(self.request, user)
        messages.success(self.request, f"Welcome {user.username}.")

        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error in registration, check your data.")
        return super().form_invalid(form)


class CustomLoginView(LoginView):
    template_name = "accounts/login_page.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("accounts:profile")

    def form_valid(self, form):
        messages.success(self.request, "You logged in successfully!")
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Logout.")
        return super().dispatch(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tasks = self.request.user.tasks

        context.update(
            {
                "total_tasks": tasks.count(),
                "done_tasks": tasks.filter(is_completed=True).count(),
                "pending_tasks": tasks.filter(is_completed=False).count(),
            }
        )

        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = "accounts/edit_profile.html"
    success_url = reverse_lazy("accounts:profile")

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Profile updated successfully!")
        return super().form_valid(form)


class HomeView(TemplateView):
    template_name = "home.html"
