from __future__ import annotations
from datetime import datetime
from src.shared.domain.vo import ValueObject


class DatetimeValueObject(ValueObject):

    def __init__(self, value: datetime):
        super(DatetimeValueObject, self).__init__(value)

    def __str__(self):
        return self.value.isoformat()

    def __repr__(self):
        return f'DatetimeValueObject({str(self.value)})'

    def __eq__(self, rhs):
        if not isinstance(rhs, DatetimeValueObject):
            return False
        return rhs.value == self.value

    def __ne__(self, rhs):
        return not (self == rhs)

    def __hash__(self):
        return hash(self.value)

    @classmethod
    def from_text(cls, value: str) -> DatetimeValueObject:
        try:
            dt = datetime.fromisoformat(value)
            return cls(dt)
        except Exception:
            raise cls._raise_validation_exception(value)

    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not a datetime')

    @classmethod
    def _validate(cls, value):
        if not isinstance(value, datetime):
            cls._raise_validation_exception(value)

    @property
    def native(self):
        return str(self.value)
