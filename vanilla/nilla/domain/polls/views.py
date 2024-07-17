from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Question, QuestionChoice
from .serializers import QuestionSerializer


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(
        detail=True,
        methods=["post"],
        url_path="vote",
        permission_classes=[IsAuthenticated],
    )
    def vote(self, request, pk=None):
        question = self.get_object()
        try:
            selected_choice = question.questionchoice_set.get(
                pk=request.data.get("choice")
            )
        except (KeyError, QuestionChoice.DoesNotExist):
            return Response(
                {"error_message": "You didn't select a choice."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            selected_choice.votes = F("votes") + 1
            selected_choice.save()
            return HttpResponseRedirect(
                reverse(
                    "polls:results",
                    args=(question.id,),
                )
            )
