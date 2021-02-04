from src.hexagonal.user.application.user_deleter import UserDeleter
from tests.src.hexagonal.user.domain.user_mother import UserMother


def test_delete_user():
    user = UserMother.create()
    # TODO 0 - inject repository and publisher

    user_deleter = UserDeleter.delete(user.id)

    # TODO 1 - test user is not in repository

    # TODO 2 - test publisher has published user message
