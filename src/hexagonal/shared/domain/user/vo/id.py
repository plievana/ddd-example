from src.shared.domain.vo.uuid import UuidValueObject


class UserId(UuidValueObject):
    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not a valid user id')
