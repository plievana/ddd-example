import inject

from src.hexagonal.user.domain.user_repository import UserRepository
from src.hexagonal.user.domain.user import User
from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.user.domain.vo.name import UserName
from src.shared.domain.bus.event.domain_event_bus import DomainEventBus


class UserCreator:
    repository = inject.attr(UserRepository)
    bus = inject.attr(DomainEventBus)

    @classmethod
    def create(cls, id: UserId, name: UserName) -> None:
        user = User.create(id=id, name=name)
        cls.bus.publish(user.pull_domain_events())
        cls.repository.save(user)
