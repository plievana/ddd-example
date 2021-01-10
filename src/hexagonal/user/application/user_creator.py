from src.hexagonal.user.domain.user_repository import UserRepository
from src.hexagonal.user.domain.user import User
from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.user.domain.vo.name import UserName


class UserCreator:
    __slots__ = ('repository',)

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create(self, id: UserId, name: UserName) -> None:
        user = User(id=id, name=name)
        self.repository.save(user)
