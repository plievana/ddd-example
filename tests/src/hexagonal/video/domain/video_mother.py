from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.video.domain.video import Video
from src.hexagonal.video.domain.vo.id import VideoId
from src.hexagonal.video.domain.vo.title import VideoTitle
from src.hexagonal.video.domain.vo.category import VideoCategory
from src.hexagonal.video.domain.vo.duration import VideoDuration
from tests.src.hexagonal.shared.domain.user.vo.id_mother import UserIdMother
from tests.src.hexagonal.video.domain.vo.category_mother import VideoCategoryMother
from tests.src.hexagonal.video.domain.vo.duration_mother import VideoDurationMother
from tests.src.hexagonal.video.domain.vo.id_mother import VideoIdMother
from tests.src.hexagonal.video.domain.vo.title_mother import VideoTitleMother


class VideoMother:
    @staticmethod
    def create(id: VideoId = None, title: VideoTitle = None, duration_in_seconds: VideoDuration = None,
               category: VideoCategory = None, creator_id: UserId = None) -> Video:
        return Video.create(
            id=id or VideoIdMother.create(),
            title=title or VideoTitleMother.create(),
            duration_in_seconds=duration_in_seconds or VideoDurationMother.create(),
            category=category or VideoCategoryMother.create(),
            creator_id=creator_id or UserIdMother.create())
