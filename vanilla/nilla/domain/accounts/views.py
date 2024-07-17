from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

User = get_user_model()


class UserCreationForm(AuthUserCreationForm):
    class Meta(AuthUserCreationForm.Meta):
        model = User


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
