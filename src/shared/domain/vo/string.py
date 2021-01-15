from __future__ import annotations
from src.shared.domain.vo import ValueObject


class StringValueObject(ValueObject):

    def __init__(self, value: str):
        super(StringValueObject, self).__init__(value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return f'StringValueObject({str(self.value)})'

    def __eq__(self, rhs):
        if not isinstance(rhs, StringValueObject):
            return False
        return rhs.value == self.value

    def __ne__(self, rhs):
        return not (self == rhs)

    def __hash__(self):
        return hash(self.value)

    @classmethod
    def from_text(cls, value: str) -> StringValueObject:
        try:
            return cls(value)
        except:
            cls._raise_validation_exception(value)

    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not a string')

    @classmethod
    def _validate(cls, value):
        if not isinstance(value, str):
            cls._raise_validation_exception(value)
