from datetime import datetime

from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.user.domain.vo.name import UserName
from src.hexagonal.user.domain.vo.updated import UserUpdated


class User:
    __slots__ = ('id', 'name', 'updated_at',)

    def __init__(self, id: UserId, name: UserName, updated_at: UserUpdated = None):
        self.id = id
        self.name = name
        self.updated_at = updated_at if updated_at else UserUpdated(datetime.now())
