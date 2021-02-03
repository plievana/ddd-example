import abc
from typing import Sequence

from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.video.domain.video import Video


class VideoRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def all(self) -> Sequence[Video]:
        raise NotImplementedError

    @abc.abstractmethod
    def save(self, video: Video) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def search_by_user_id(self, user_id: UserId) -> Sequence[Video]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_one(self, video: Video) -> None:
        raise NotImplementedError
