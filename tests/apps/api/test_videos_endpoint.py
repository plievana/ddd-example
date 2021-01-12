import uuid
import json
import random
from http import HTTPStatus

import pytest
import inject

from src.hexagonal.video.domain.video import Video
from src.hexagonal.video.domain.video_repository import VideoRepository
from src.hexagonal.video.domain.vo.id import VideoId
from src.hexagonal.video.domain.vo.title import VideoTitle
from src.hexagonal.video.domain.vo.duration import VideoDuration
from src.hexagonal.video.domain.vo.category import VideoCategory
from src.hexagonal.shared.domain.user.vo.id import UserId
from apps.api.encoders.video import VideoEncoder


@pytest.mark.usefixtures("mongo_client")
class TestVideosEndpoint:
    repository = inject.attr(VideoRepository)

    def setup(self):
        self.mongo_client.db.users.drop()

    def test_get(self, client):
        """
        return all the videos getting("/videos")
        """
        for i in range(0, random.randint(1, 10)):
            video = Video(
                id=VideoId(uuid.uuid4()),
                title=VideoTitle(f"Video {i}"),
                duration_in_seconds=VideoDuration(random.randint(10, 1000)),
                category=VideoCategory(VideoCategory.INTERVIEW),
                creator_id=UserId(uuid.uuid4())
            )

            self.repository.save(video)

        response = client.get("/videos")
        assert response.status_code == HTTPStatus.OK
        assert response.headers['Content-Type'] == 'application/json'
        assert json.loads(response.data) == [VideoEncoder.encode(v) for v in self.repository.all()]

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
