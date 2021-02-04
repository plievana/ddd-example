from src.hexagonal.video.domain.vo.id import VideoId
from tests.src.shared.domain.vo.uuid_mother import UuidMother


class VideoIdMother:

    def create(self, id: str = None):
        return VideoId(id or UuidMother.create())
