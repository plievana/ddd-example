import uuid
from src.shared.domain.vo import ValueObject


class UuidValueObject(ValueObject):

    def __init__(self, value):
        super().__init__(value)
        self._value = uuid.UUID(value, version=4) if isinstance(value, str) else value

    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not an UUID')

    @classmethod
    def _validate(cls, value):
        if not isinstance(value, uuid.UUID):
            try:
                value = uuid.UUID(value, version=4)
            except ValueError:
                cls._raise_validation_exception(value)

    @property
    def native(self):
        return str(self.value)
