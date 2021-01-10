from src.shared.domain.vo.datetime import DatetimeValueObject


class VideoUpdated(DatetimeValueObject):
    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not a valid datetime for updated video field')