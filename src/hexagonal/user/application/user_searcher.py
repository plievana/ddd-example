import inject
from typing import Sequence
from src.hexagonal.user.domain.user_repository import UserRepository
from src.hexagonal.user.domain.user import User


class UserSearcher:
    repository = inject.attr(UserRepository)

    @classmethod
    def all(cls) -> Sequence[User]:
        return cls.repository.all()
