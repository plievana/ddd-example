import inject

from src.hexagonal.user.domain.user_repository import UserRepository
from src.hexagonal.user.domain.user import User
from src.hexagonal.shared.domain.user.vo.id import UserId
from src.shared.domain.bus.event.domain_event_bus import DomainEventBus


class UserDeleter:
    repository = inject.attr(UserRepository)
    bus = inject.attr(DomainEventBus)

    @classmethod
    def delete(cls, id: UserId) -> None:
        user = User.delete(id=id)
        cls.bus.publish(user.pull_domain_events())
        cls.repository.delete_one(user)
