from typing import Sequence

from src.shared.infrastructure.mongo_connection import MongoDB
from src.hexagonal.video.domain.video import Video
from src.hexagonal.video.domain.video_repository import VideoRepository

from src.hexagonal.video.domain.vo.id import VideoId
from src.hexagonal.video.domain.vo.title import VideoTitle
from src.hexagonal.video.domain.vo.duration import VideoDuration
from src.hexagonal.video.domain.vo.category import VideoCategory
from src.hexagonal.video.domain.vo.updated import VideoUpdated
from src.hexagonal.shared.domain.user.vo.id import UserId


def create_video_from_dict(d):
    return Video(
                id=VideoId(d.get('video_id')),
                title=VideoTitle(d.get('title')),
                duration_in_seconds=VideoDuration(d.get('duration_in_seconds')),
                category=VideoCategory(d.get('category')),
                creator_id=UserId(d.get('creator_id')),
                updated_at=VideoUpdated(d.get('updated_at'))
            )

class MongoVideoRepository(VideoRepository):
    __slots__ = ('_collection',)
    _COLLECTION_NAME = 'video'

    def __init__(self, db_connection: MongoDB):
        self._collection = db_connection.db[MongoVideoRepository._COLLECTION_NAME]

    def all(self) -> Sequence[Video]:
        for v_dict in self._collection.find():
            yield create_video_from_dict(v_dict)

    def save(self, video: Video) -> None:
        video_dict = {
            'video_id': video.id.value,
            'title': video.title.value,
            'duration_in_seconds': video.duration_in_seconds.value,
            'category': video.category.value,
            'creator_id': video.creator_id.value,
            'updated_at': video.updated_at.value
        }
        self._collection.save(video_dict)

    def search_by_user_id(self, user_id: UserId) -> Sequence[Video]:
        query = {
            'creator_id': user_id
        }
        for v_dict in self._collection.find(query):
            yield create_video_from_dict(v_dict)

    def delete_one(self, video: Video) -> None:
        video_dict = {
            'video_id': video.id.value
        }
        self._collection.delete_one(video_dict)
