from django.db import models

from .question import Question


class QuestionChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        db_table = "polls_questionchoice"
