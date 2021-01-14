from __future__ import annotations
from datetime import datetime

from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.user.domain.user_domain_event import UserCreatedDomainEvent
from src.hexagonal.user.domain.vo.name import UserName
from src.hexagonal.user.domain.vo.updated import UserUpdated
from src.shared.domain.aggregate.aggregate_root import AggregateRoot


class User(AggregateRoot):
    __slots__ = ('id', 'name', 'updated_at',)

    def __init__(self, id: UserId, name: UserName, updated_at: UserUpdated = None):
        self.id = id
        self.name = name
        self.updated_at = updated_at if updated_at else UserUpdated(datetime.now())
        super(User, self).__init__()

    @staticmethod
    def create(id: UserId, name: UserName) -> User:
        user = User(id, name)
        user._record(UserCreatedDomainEvent(id.value, name.value))
        return user

