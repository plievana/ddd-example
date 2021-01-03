import uuid
import json
import random
from http import HTTPStatus
from app.models.user import User
from app.repositories.user_repository import UserRepository


class TestUsersEndpoint:
    def setup(self):
        from app import db
        db.user.drop()

    def test_get(self, client):
        """
        return all the users getting("/users")
        """
        users = []
        for i in range(0, random.randint(1, 10)):
            user = User().load({"id": uuid.uuid4(), "name": f"User {i}"})
            users.append(user)
            UserRepository().save(user)

        response = client.get("/users")
        assert response.status_code == HTTPStatus.OK
        assert response.headers['Content-Type'] == 'application/json'
        assert json.loads(response.data) == UserRepository().all()

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
