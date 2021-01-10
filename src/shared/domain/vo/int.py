from src.shared.domain.vo import ValueObject


class IntValueObject(ValueObject):

    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not an integer')

    @classmethod
    def _validate(cls, value):
        if not isinstance(value, int):
            cls._raise_validation_exception(value)
