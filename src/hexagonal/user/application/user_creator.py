import inject

from src.hexagonal.user.domain.user_repository import UserRepository
from src.hexagonal.user.domain.user import User
from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.user.domain.vo.name import UserName


class UserCreator:
    repository = inject.attr(UserRepository)

    @classmethod
    def create(cls, id: UserId, name: UserName) -> None:
        user = User(id=id, name=name)
        cls.repository.save(user)
