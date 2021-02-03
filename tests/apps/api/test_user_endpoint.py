import uuid
from http import HTTPStatus

import pytest
import inject

from src.hexagonal.user.domain.user import User
from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.user.domain.user_repository import UserRepository
from src.hexagonal.user.domain.vo.name import UserName


@pytest.mark.usefixtures("mongo_client")
class TestUserEndpoint:
    repository = inject.attr(UserRepository)

    def setup(self):
        self.mongo_client.db.users.drop()

    def test_delete(self, client):
        """
        Delete user
        """
        user_id = uuid.uuid4()
        user = User(id=UserId(user_id),
                    name=UserName(f"User"))
        self.repository.save(user)

        response = client.delete(f"/user/{user_id}")
        assert response.status_code == HTTPStatus.NO_CONTENT

    def test_post(self, client):
        """
        Create a new video posting("/users")
        """
        user_payload = {
            "id": str(uuid.uuid4()),
            "name": "Test user"
        }
        response = client.post("/users", json=user_payload)
        assert response.status_code == HTTPStatus.NO_CONTENT
