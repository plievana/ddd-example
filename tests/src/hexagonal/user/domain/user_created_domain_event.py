from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.user.domain.user import User
from src.hexagonal.user.domain.user_domain_event import UserCreatedDomainEvent, UserDeletedDomainEvent
from src.hexagonal.user.domain.vo.name import UserName
from tests.src.hexagonal.shared.domain.user.vo.id_mother import UserIdMother
from tests.src.hexagonal.user.domain.vo.name_mother import UserNameMother


class UserCreatedDomainEventMother:

    @classmethod
    def create(cls, id: UserId = None, name: UserName = None) -> UserCreatedDomainEvent:
        return UserCreatedDomainEvent(
            id=id.native if id is not None else UserIdMother.create().native,
            name=name.value if name is not None else UserNameMother.create().native,
        )

    @classmethod
    def from_user(cls, user: User) -> UserCreatedDomainEvent:
        return cls.create(user.id, user.name)


class UserDeletedDomainEventMother:

    @classmethod
    def create(cls, id: UserId = None, name: UserName = None) -> UserDeletedDomainEvent:
        return UserDeletedDomainEvent(
            id=id.native if id is not None else UserIdMother.create().native,
        )

    @classmethod
    def from_user(cls, user: User) -> UserDeletedDomainEvent:
        return cls.create(user.id, user.name)
