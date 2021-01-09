from typing import Sequence

from src.shared.infrastructure.mongo_connection import MongoDB
from src.hexagonal.user.domain.user import User
from src.hexagonal.user.domain.user_repository import UserRepository


class MongoUserRepository(UserRepository):
    __slots__ = ('_collection',)
    _COLLECTION_NAME = 'user'

    def __init__(self, db_connection: MongoDB):
        self._collection = db_connection.db[MongoUserRepository._COLLECTION_NAME]

    def all(self) -> Sequence[User]:
        return User(many=True).dump(self._collection.find())

    def save(self, user: User) -> None:
        self._collection.save(user)
