from urllib.parse import urlparse
from src.shared.domain.vo import ValueObject


class UrlValueObject(ValueObject):

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

    def __str__(self) -> str:
        return str(self._value)
