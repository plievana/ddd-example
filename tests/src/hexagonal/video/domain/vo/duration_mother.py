from src.hexagonal.video.domain.vo.duration import VideoDuration
from tests.src.shared.domain.vo.int_mother import IntegerMother


class VideoDurationMother(object):
    @classmethod
    def create(cls, value: str = None) -> VideoDuration:
        return VideoDuration(value if value else IntegerMother.create())
