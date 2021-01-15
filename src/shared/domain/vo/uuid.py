from __future__ import annotations
import uuid
from src.shared.domain.vo import ValueObject


class UuidValueObject(ValueObject):

    def __init__(self, value: uuid.UUID):
        super(UuidValueObject, self).__init__(value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return f'UuidValueObject({str(self.value)})'

    def __eq__(self, rhs):
        if not isinstance(rhs, UuidValueObject):
            return False
        return rhs.value == self.value

    def __ne__(self, rhs):
        return not (self == rhs)

    def __hash__(self):
        return hash(self.value)

    @classmethod
    def from_text(cls, value: str) -> UuidValueObject:
        try:
            return cls(uuid.UUID(value, version=4))
        except:
            cls._raise_validation_exception(value)

    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not an UUID')

    @classmethod
    def _validate(cls, value):
        if not isinstance(value, uuid.UUID):
            cls._raise_validation_exception(value)

    @property
    def native(self):
        return str(self.value)
