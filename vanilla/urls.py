from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("vanilla.nilla.services.polls.urls")),
    path("admin/", admin.site.urls),
]
