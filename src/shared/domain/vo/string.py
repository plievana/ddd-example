from src.shared.domain.vo import ValueObject


class StringValueObject(ValueObject):

    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not a string')

    @classmethod
    def _validate(cls, value):
        if not isinstance(value, str):
            cls._raise_validation_exception(value)
