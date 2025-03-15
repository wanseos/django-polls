import typing as t

T = t.TypeVar("T")
E = t.TypeVar("E")


class Result(t.Generic[T, E]):
    def __init__(self, value: t.Union[T, None] = None, error: t.Union[E, None] = None):
        self.value = value
        self.error = error

    def is_ok(self) -> bool:
        return self.error is None

    def is_error(self) -> bool:
        return self.error is not None
