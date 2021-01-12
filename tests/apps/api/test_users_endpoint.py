import uuid
import json
import random
from http import HTTPStatus

import pytest
import inject

from src.hexagonal.user.domain.user import User
from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.user.domain.user_repository import UserRepository
from src.hexagonal.user.domain.vo.name import UserName
from apps.api.encoders.user import UserEncoder


@pytest.mark.usefixtures("mongo_client")
class TestUsersEndpoint:
    repository = inject.attr(UserRepository)

    def setup(self):
        self.mongo_client.db.users.drop()

    def test_get(self, client):
        """
        return all the users getting("/users")
        """
        for i in range(0, random.randint(1, 10)):
            user = User(id=UserId(uuid.uuid4()),
                        name=UserName(f"User {i}"))
            self.repository.save(user)
        response = client.get("/users")
        assert response.status_code == HTTPStatus.OK
        assert response.headers['Content-Type'] == 'application/json'
        assert json.loads(response.data) == [UserEncoder.encode(u) for u in self.repository.all()]

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
