import uuid
import json
import random
from http import HTTPStatus

import pytest

from src.hexagonal.video.domain.video import Video
from src.hexagonal.video.infrastructure.repository.mongo_video_repository import MongoVideoRepository


@pytest.mark.usefixtures("mongo_client")
class TestVideosEndpoint:
    def setup(self):
        self.mongo_client.db.users.drop()
        self.repository = MongoVideoRepository(self.mongo_client)

    def test_get(self, client):
        """
        return all the videos getting("/videos")
        """
        for i in range(0, random.randint(1, 10)):
            video_dict = {
                "id": uuid.uuid4(),
                "title": f"Video {i}",
                "duration_in_seconds": random.randint(10, 1000),
                "category": "Screencast",
                "creator_id": uuid.uuid4()
            }

            video = Video().load(video_dict)
            self.repository.save(video)

        response = client.get("/videos")
        assert response.status_code == HTTPStatus.OK
        assert response.headers['Content-Type'] == 'application/json'
        assert json.loads(response.data) == self.repository.all()

    def test_post(self, client):
        """
        Create a new video posting("/videos")
        """
        video_payload = {
            "id": str(uuid.uuid4()),
            "title": "Test Video",
            "duration_in_seconds": 969,
            "category": "Screencast",
            "creator_id": str(uuid.uuid4())
        }
        response = client.post("/videos", json=video_payload)
        assert response.status_code == HTTPStatus.NO_CONTENT
