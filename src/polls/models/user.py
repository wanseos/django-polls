from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = "polls_user"
