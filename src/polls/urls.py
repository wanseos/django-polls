from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path(
        "",
        views.handle_list_create,
        name="list-create",
    ),
    path(
        "<int:pk>",
        views.handle_detail_update_delete,
        name="detail-update-delete",
    ),
    path(
        "<int:pk>/vote",
        views.handle_vote,
        name="vote",
    ),
]
