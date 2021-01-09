from src.shared.infrastructure.db_connection import DBConnection
from src.hexagonal.video.domain.video_repository import VideoRepository
from src.hexagonal.video.infrastructure.repository.mongo_video_repository import MongoVideoRepository
from src.hexagonal.video.application.video_searcher import VideoSearcher
from src.hexagonal.video.application.video_creator import VideoCreator


class VideoModuleDependencyContainer:
    __slots__ = ('db_connection',)

    def __init__(self, db_connection: DBConnection):
        self.db_connection = db_connection

    @property
    def _repository(self) -> VideoRepository:
        return MongoVideoRepository(self.db_connection)

    @property
    def video_searcher(self) -> VideoSearcher:
        return VideoSearcher(self._repository)

    @property
    def video_creator(self) -> VideoCreator:
        return VideoCreator(self._repository)