from typing import Sequence
import inject

from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.user.domain.user_domain_event import UserDeletedDomainEvent
from src.hexagonal.video.application.delete.video_deleter import VideoDeleter
from src.hexagonal.video.domain.video_repository import VideoRepository
from src.shared.domain.bus.event.domain_event_subscriber import DomainEventSubscriber


class DeleteVideoOnUserDeleted(DomainEventSubscriber):
    repository = inject.attr(VideoRepository)

    def __init__(self, deleter: VideoDeleter):
        self._deleter = deleter

    @classmethod
    def subscribed_to(cls) -> Sequence:
        return [UserDeletedDomainEvent]

    def invoke(self, event: UserDeletedDomainEvent) -> None:
        user_id = UserId.from_text(event.id)
        for video in self.repository.search_by_user_id(user_id):
            self._deleter.delete(video.id)

