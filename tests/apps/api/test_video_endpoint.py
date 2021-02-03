import uuid
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


@pytest.mark.usefixtures("mongo_client")
class TestVideoEndpoint:
    repository = inject.attr(VideoRepository)

    def setup(self):
        self.mongo_client.db.users.drop()

    def test_delete(self, client):
        """
        Delete video
        """
        video_id = uuid.uuid4()
        video = Video(
            id=VideoId(video_id),
            title=VideoTitle(f"Video"),
            duration_in_seconds=VideoDuration(random.randint(10, 1000)),
            category=VideoCategory(VideoCategory.INTERVIEW),
            creator_id=UserId(uuid.uuid4())
        )
        self.repository.delete_one(video)

        response = client.delete(f"/video/{video_id}")
        assert response.status_code == HTTPStatus.NO_CONTENT