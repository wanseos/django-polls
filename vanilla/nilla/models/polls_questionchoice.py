from django.db import models

from .polls_question import Question


class QuestionChoice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
    choice_text = models.CharField(max_length=200)

    class Meta:
        db_table = "polls_questionchoice"
