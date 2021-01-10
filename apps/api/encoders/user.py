from src.hexagonal.user.domain.user import User


class UserEncoder(list):
    @staticmethod
    def encode(user: User) -> dict:
        return {
            'id': user.id.native,
            'name': user.name.native,
            'updated_at': user.updated_at.native
        }
