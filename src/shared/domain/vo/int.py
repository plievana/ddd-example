from __future__ import annotations
from src.shared.domain.vo import ValueObject


class IntValueObject(ValueObject):

    def __init__(self, value: int):
        super(IntValueObject, self).__init__(value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return f'IntValueObject({str(self.value)})'

    def __eq__(self, rhs):
        if not isinstance(rhs, IntValueObject):
            return False
        return rhs.value == self.value

    def __ne__(self, rhs):
        return not (self == rhs)

    def __hash__(self):
        return hash(self.value)

    @classmethod
    def from_text(cls, value: str) -> IntValueObject:
        try:
            return cls(int(value))
        except:
            cls._raise_validation_exception(value)

    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not an integer')

    @classmethod
    def _validate(cls, value):
        if not isinstance(value, int):
            cls._raise_validation_exception(value)
