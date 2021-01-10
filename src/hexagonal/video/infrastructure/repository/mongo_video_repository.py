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


class MongoVideoRepository(VideoRepository):
    __slots__ = ('_collection',)
    _COLLECTION_NAME = 'video'

    def __init__(self, db_connection: MongoDB):
        self._collection = db_connection.db[MongoVideoRepository._COLLECTION_NAME]

    def all(self) -> Sequence[Video]:
        for v_dict in self._collection.find():
            v = Video(
                id=VideoId(v_dict.get('video_id')),
                title=VideoTitle(v_dict.get('title')),
                duration_in_seconds=VideoDuration(v_dict.get('duration_in_seconds')),
                category=VideoCategory(v_dict.get('category')),
                creator_id=UserId(v_dict.get('creator_id')),
                updated_at=VideoUpdated(v_dict.get('updated_at'))
            )
            yield v

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
