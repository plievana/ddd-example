from typing import Sequence
from app import db

from app.models.user import User


class UserRepository:
    __slots__ = ('_c', )
    _COLLECTION_NAME = 'user'

    def __init__(self):
        self._c = db[UserRepository._COLLECTION_NAME]
  
    def all(self) -> Sequence[User]:
        return User(many=True).dump(self._c.find())

    def save(self, user: User) -> User:
        return self._c.save(user)
