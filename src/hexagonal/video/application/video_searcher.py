from typing import Sequence
import inject
from src.hexagonal.video.domain.video_repository import VideoRepository
from src.hexagonal.video.domain.video import Video


class VideoSearcher:
    repository = inject.attr(VideoRepository)

    @classmethod
    def all(cls) -> Sequence[Video]:
        return cls.repository.all()
