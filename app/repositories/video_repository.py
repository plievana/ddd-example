from typing import Sequence
from app import db

from app.models.video import Video


class VideoRepository:
    __slots__ = ('_c', )
    _COLLECTION_NAME = 'video'

    def __init__(self):
        self._c = db[VideoRepository._COLLECTION_NAME]

    def all(self) -> Sequence[Video]:
        return Video(many=True).dump(self._c.find())

    def save(self, video: Video) -> Video:
        return self._c.save(video)
