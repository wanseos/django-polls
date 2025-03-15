from django.test import TestCase
from django.urls import reverse

from ..models import Question, QuestionChoice


class PollsAPITest(TestCase):
    def setUp(self) -> None:
        self.question = Question.objects.create(content="Favorite color?")
        self.choice1 = QuestionChoice.objects.create(
            question=self.question, content="Red"
        )
        self.choice2 = QuestionChoice.objects.create(
            question=self.question, content="Blue"
        )

    def test_polls_detail(self):
        response = self.client.get(
            reverse("polls:detail-update-delete", args=[self.question.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_polls_list(self):
        response = self.client.get(reverse("polls:list-create"))
        self.assertEqual(response.status_code, 200)

    def test_polls_create(self):
        response = self.client.post(
            reverse("polls:list-create"), {"content": "Favorite animal?"}
        )
        self.assertEqual(response.status_code, 201)

    def test_polls_update(self):
        response = self.client.post(
            reverse("polls:detail-update-delete", args=[self.question.pk]),
            {"content": "Favorite food?"},
        )
        self.assertEqual(response.status_code, 200)

    def test_polls_delete(self):
        response = self.client.delete(
            reverse("polls:detail-update-delete", args=[self.question.pk])
        )
        self.assertEqual(response.status_code, 204)

    def test_polls_vote(self):
        response = self.client.post(
            reverse("polls:vote", args=[self.question.pk]),
            {"choice_id": self.choice1.pk},
        )
        self.assertEqual(response.status_code, 200)
