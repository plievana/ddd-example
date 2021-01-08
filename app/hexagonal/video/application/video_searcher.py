from typing import Sequence
from app.hexagonal.video.domain.video_repository import VideoRepository
from app.hexagonal.video.domain.video import Video


class VideoSearcher:
    __slots__ = ('repository',)

    def __init__(self, repository: VideoRepository):
        self.repository = repository

    def all(self) -> Sequence[Video]:
        return self.repository.all()
