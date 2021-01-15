from __future__ import annotations
from urllib.parse import urlparse
from src.shared.domain.vo import ValueObject


class UrlValueObject(ValueObject):

    def __init__(self, value: str):
        super(UrlValueObject, self).__init__(value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return f'UrlValueObject({str(self.value)})'

    def __eq__(self, rhs):
        if not isinstance(rhs, UrlValueObject):
            return False
        return rhs.value == self.value

    def __ne__(self, rhs):
        return not (self == rhs)

    def __hash__(self):
        return hash(self.value)

    @classmethod
    def from_text(cls, value: str) -> UrlValueObject:
        try:
            return cls(value)
        except:
            cls._raise_validation_exception(value)

    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not a valid url')

    @classmethod
    def _validate(cls, value):
        try:
            result = urlparse(value)
            if not all([result.scheme, result.netloc, result.path]):
                raise Exception()
        except:
            cls._raise_validation_exception(value)
