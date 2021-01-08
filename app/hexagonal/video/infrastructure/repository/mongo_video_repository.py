from typing import Sequence

from app.hexagonal.shared.infrastructure.mongo_connection import MongoDB
from app.hexagonal.video.domain.video import Video
from app.hexagonal.video.domain.video_repository import VideoRepository


class MongoVideoRepository(VideoRepository):
    __slots__ = ('_collection',)
    _COLLECTION_NAME = 'video'

    def __init__(self, db_connection: MongoDB):
        self._collection = db_connection.db[MongoVideoRepository._COLLECTION_NAME]

    def all(self) -> Sequence[Video]:
        return Video(many=True).dump(self._collection.find())

    def save(self, video: Video) -> None:
        self._collection.save(video)
