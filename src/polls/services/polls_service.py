import typing as t

from corelib import Result

from . import question_choice_service, question_service


class RetrieveDetailData(t.TypedDict):
    pk: int
    content: str


def retrieve_detail(pk: int) -> RetrieveDetailData:
    obj = question_service.query_one(pk)
    return {"pk": obj.pk, "content": obj.content}


class RetrieveListDataItem(t.TypedDict):
    pk: int
    content: str


class RetrieveListData(t.TypedDict):
    data: t.List[RetrieveListDataItem]


def retrieve_list() -> RetrieveListData:
    objs = question_service.query_all()
    return {"data": [{"pk": obj.pk, "content": obj.content} for obj in objs]}


class AddData(t.TypedDict):
    pk: int
    content: str


def add(content: str) -> AddData:
    obj = question_service.create(content)
    return {"pk": obj.pk, "content": obj.content}


class ModifyData(t.TypedDict):
    pk: int
    content: str


def modify(pk: int, content: str) -> Result[ModifyData, str]:
    if not _is_valid_modify_input(content):
        return Result(error="Invalid input")
    obj = question_service.update(pk, content)
    return Result(value={"pk": obj.pk, "content": obj.content})


def _is_valid_modify_input(content: str) -> bool:
    if not content.strip():
        return False
    return True


class RemoveData(t.TypedDict):
    deleted: int


def remove(pk: int) -> RemoveData:
    result = question_service.delete(pk)
    return {"deleted": result[0]}


class VoteData(t.TypedDict):
    votes: int


def vote(question_id: int, choice_id: int) -> VoteData:
    obj = question_choice_service.vote(question_id, choice_id)
    return VoteData(votes=obj.votes)
