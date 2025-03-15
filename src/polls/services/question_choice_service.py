from ..models import QuestionChoice


def vote(question_id: int, choice_id: int) -> QuestionChoice:
    choice = QuestionChoice.objects.get(pk=choice_id, question_id=question_id)
    choice.votes += 1
    choice.save()
    return choice
