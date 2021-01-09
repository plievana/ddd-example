import uuid
import json
import random
from http import HTTPStatus

import pytest

from src.hexagonal.user.domain.user import User
from src.hexagonal.user.infrastructure.repository.mongo_user_repository import MongoUserRepository


@pytest.mark.usefixtures("mongo_client")
class TestUsersEndpoint:
    def setup(self):
        self.mongo_client.db.users.drop()
        self.repository = MongoUserRepository(self.mongo_client)

    def test_get(self, client):
        """
        return all the users getting("/users")
        """
        for i in range(0, random.randint(1, 10)):
            user = User().load({"id": uuid.uuid4(), "name": f"User {i}"})
            self.repository.save(user)
        response = client.get("/users")
        assert response.status_code == HTTPStatus.OK
        assert response.headers['Content-Type'] == 'application/json'
        assert json.loads(response.data) == self.repository.all()

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
