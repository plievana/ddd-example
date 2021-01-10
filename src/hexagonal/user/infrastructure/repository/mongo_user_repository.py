from typing import Sequence

from src.shared.infrastructure.mongo_connection import MongoDB
from src.hexagonal.user.domain.user import User
from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.user.domain.vo.name import UserName
from src.hexagonal.user.domain.vo.updated import UserUpdated
from src.hexagonal.user.domain.user_repository import UserRepository


class MongoUserRepository(UserRepository):
    __slots__ = ('_collection',)
    _COLLECTION_NAME = 'user'

    def __init__(self, db_connection: MongoDB):
        self._collection = db_connection.db[MongoUserRepository._COLLECTION_NAME]

    def all(self) -> Sequence[User]:
        for u in self._collection.find():
            u = User(id=UserId(u.get('user_id')),
                     name=UserName(u.get('name')),
                     updated_at=UserUpdated(u.get('updated_at')))
            yield u

    def save(self, user: User) -> None:
        user_dict = {
            'user_id': user.id.value,
            'name': user.name.value,
            'updated_at': user.updated_at.value
        }
        self._collection.save(user_dict)
