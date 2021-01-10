from datetime import datetime
from src.shared.domain.vo import ValueObject


class DatetimeValueObject(ValueObject):

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
