from __future__ import annotations
import abc


class ValueObject(abc.ABC):

    def __init__(self, value):
        self.__class__._validate(value)
        self.value = value

    @classmethod
    def replace(cls, value):
        return cls(value)

    @classmethod
    @abc.abstractmethod
    def _validate(cls, value):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def from_text(cls, value: str) -> ValueObject:
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def _raise_validation_exception(cls, value):
        raise NotImplementedError

    @property
    def native(self):
        return self.value
