from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.user.domain.user import User
from src.hexagonal.user.domain.vo.name import UserName
from tests.src.hexagonal.shared.domain.user.vo.id_mother import UserIdMother
from tests.src.hexagonal.user.domain.vo.name_mother import UserNameMother


class UserMother:
    @staticmethod
    def create(id: UserId = None, name: UserName = None) -> User:
        return User.create(
            id=id or UserIdMother.create(),
            name=name or UserNameMother.create())
