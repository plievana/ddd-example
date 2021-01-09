import abc
from typing import Sequence
from src.hexagonal.video.domain.video import Video


class VideoRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def all(self) -> Sequence[Video]:
        raise NotImplementedError

    @abc.abstractmethod
    def save(self, video: Video) -> None:
        raise NotImplementedError
