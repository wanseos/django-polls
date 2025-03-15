import typing as t

from ..models import Question


def query_one(pk: int) -> Question:
    return Question.objects.get(pk=pk)


def query_all() -> t.Iterable[Question]:
    return Question.objects.all()


def create(content: str) -> Question:
    obj = Question(content=content)
    obj.save()
    return obj


def update(pk: int, content: str) -> Question:
    obj = Question.objects.get(pk=pk)
    obj.content = content
    obj.save()
    return obj


def delete(pk: int) -> tuple:
    obj = Question.objects.get(pk=pk)

    return obj.delete()
