from src.shared.domain.vo.int import IntValueObject


class VideoDuration(IntValueObject):
    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not a valid duration (seconds)')
