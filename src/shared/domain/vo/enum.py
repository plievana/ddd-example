from __future__ import annotations
import inspect
import re
from src.shared.domain.vo import ValueObject

REGEX = re.compile(r'^__.*__$')


class EnumValueObject(ValueObject):

    def __init__(self, value: str):
        super(EnumValueObject, self).__init__(value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return f'EnumValueObject({str(self.value)})'

    def __eq__(self, rhs):
        if not isinstance(rhs, EnumValueObject):
            return False
        return rhs.value == self.value

    def __ne__(self, rhs):
        return not (self == rhs)

    def __hash__(self):
        return hash(self.value)

    @classmethod
    def from_text(cls, value: str) -> EnumValueObject:
        return cls(value)

    @classmethod
    def _validate(cls, value):
        for k, v in inspect.getmembers(cls):
            if not REGEX.match(k) and not callable(v) and v == value:
                return True

        cls._raise_validation_exception(value)

    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not a valid value')
