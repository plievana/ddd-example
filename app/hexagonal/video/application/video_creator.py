from app.hexagonal.video.domain.video_repository import VideoRepository
from app.hexagonal.video.domain.video import Video


class VideoCreator:
    __slots__ = ('repository',)

    def __init__(self, repository: VideoRepository):
        self.repository = repository

    def create(self, id: str, title: str, duration_in_seconds: int, category: str, creator_id: str) -> None:
        video_dict = {
            "id": id,
            "title": title,
            "duration_in_seconds": duration_in_seconds,
            "category": category,
            "creator_id": creator_id
        }
        video = Video().load(video_dict)
        self.repository.save(video)
