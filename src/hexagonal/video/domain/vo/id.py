from src.shared.domain.vo.uuid import UuidValueObject


class VideoId(UuidValueObject):
    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not a valid video id')
