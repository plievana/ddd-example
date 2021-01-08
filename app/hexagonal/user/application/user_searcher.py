from typing import Sequence
from app.hexagonal.user.domain.user_repository import UserRepository
from app.hexagonal.user.domain.user import User


class UserSearcher:
    __slots__ = ('repository',)

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def all(self) -> Sequence[User]:
        return self.repository.all()
