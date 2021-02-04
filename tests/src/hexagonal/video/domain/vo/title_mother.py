from src.hexagonal.video.domain.vo.title import VideoTitle
from tests.src.shared.domain.vo.string_mother import StringMother


class VideoTitleMother(object):
    @classmethod
    def create(cls, value: str = None) -> VideoTitle:
        return VideoTitle(value if value else StringMother.create())
