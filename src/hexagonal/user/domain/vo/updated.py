from src.shared.domain.vo.datetime import DatetimeValueObject


class UserUpdated(DatetimeValueObject):
    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not a valid date for updated user field')