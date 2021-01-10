from src.shared.domain.vo.string import StringValueObject


class UserName(StringValueObject):
    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not a valid user name')