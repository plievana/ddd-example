from src.hexagonal.user.domain.vo.name import UserName
from tests.src.shared.domain.vo.string_mother import StringMother


class UserNameMother(object):
    @classmethod
    def create(cls, value: str = None) -> UserName:
        return UserName(value if value else StringMother.create())
