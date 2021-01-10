from src.shared.domain.vo.string import StringValueObject


class VideoTitle(StringValueObject):
    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not a valid video title')