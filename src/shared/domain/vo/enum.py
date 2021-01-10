import inspect
import re
from src.shared.domain.vo import ValueObject

REGEX = re.compile(r'^__.*__$')


class EnumValueObject(ValueObject):

    @classmethod
    def _validate(cls, value):
        for k, v in inspect.getmembers(cls):
            if not REGEX.match(k) and not callable(v) and v == value:
                return True

        cls._raise_validation_exception(value)

    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not a valid value')
