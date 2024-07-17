from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path("accounts/", include("vanilla.nilla.services.accounts.urls")),
    path("polls/", include("vanilla.nilla.services.polls.urls")),
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
