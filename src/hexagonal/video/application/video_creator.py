import inject

from src.hexagonal.video.domain.video_repository import VideoRepository
from src.hexagonal.video.domain.video import Video
from src.hexagonal.video.domain.vo.id import VideoId
from src.hexagonal.video.domain.vo.title import VideoTitle
from src.hexagonal.video.domain.vo.duration import VideoDuration
from src.hexagonal.video.domain.vo.category import VideoCategory
from src.hexagonal.shared.domain.user.vo.id import UserId


class VideoCreator:
    repository = inject.attr(VideoRepository)

    @classmethod
    def create(cls, id: VideoId, title: VideoTitle, duration_in_seconds: VideoDuration,
               category: VideoCategory, creator_id: UserId) -> None:
        video = Video(id=id, title=title, duration_in_seconds=duration_in_seconds, category=category,
                      creator_id=creator_id)
        cls.repository.save(video)
