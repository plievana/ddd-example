from src.hexagonal.shared.domain.user.vo.id import UserId
from tests.src.shared.domain.vo.uuid_mother import UuidMother


class UserIdMother:

    def create(self, id: str = None):
        return UserId(id or UuidMother.create())
