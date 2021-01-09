from src.hexagonal.user.domain.user_repository import UserRepository
from src.hexagonal.user.domain.user import User


class UserCreator:
    __slots__ = ('repository',)

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create(self, id: str, name: str) -> None:
        user = User().load({'id': id, 'name': name})
        self.repository.save(user)
