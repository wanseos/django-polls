from django.db import models


class Question(models.Model):
    content = models.CharField(max_length=200)

    class Meta:
        db_table = "polls_question"
