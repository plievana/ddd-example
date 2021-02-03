import inject

from src.hexagonal.video.domain.video_repository import VideoRepository
from src.hexagonal.video.domain.video import Video
from src.hexagonal.video.domain.vo.id import VideoId
from src.shared.domain.bus.event.domain_event_bus import DomainEventBus


class VideoDeleter:
    repository = inject.attr(VideoRepository)
    bus = inject.attr(DomainEventBus)

    @classmethod
    def delete(cls, id: VideoId) -> None:
        video = Video.delete(id=id)
        cls.bus.publish(video.pull_domain_events())
        cls.repository.delete_one(video)
