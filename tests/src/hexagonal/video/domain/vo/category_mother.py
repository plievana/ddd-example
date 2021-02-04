from src.hexagonal.video.domain.vo.category import VideoCategory
from tests.src.shared.domain.vo.enum_mother import EnumMother


class VideoCategoryMother(object):
    @classmethod
    def create(cls, value: str = None) -> VideoCategory:
        return VideoCategory(value if value else EnumMother.create())
