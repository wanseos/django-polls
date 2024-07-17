from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
]

router = DefaultRouter()
router.register(r"", views.QuestionViewSet, basename="question")
urlpatterns += router.urls
