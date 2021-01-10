from src.shared.domain.vo.enum import EnumValueObject


class VideoCategory(EnumValueObject):
    SCREENCAST = 'Screencast'
    INTERVIEW = 'Interview'

    @classmethod
    def _raise_validation_exception(cls, value):
        raise ValueError(f'{value} is not a valid video category')
