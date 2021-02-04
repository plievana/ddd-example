from src.hexagonal.user.application.user_creator import UserCreator
from tests.src.hexagonal.user.domain.user_mother import UserMother


def test_create_user():
    user = UserMother.create()
    # TODO 0 - inject repository and publisher

    user_creator = UserCreator.create(user.id, user.name)

    # TODO 1 - test user is in repository

    # TODO 2 - test publisher has published user message
