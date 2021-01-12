from __future__ import annotations
from datetime import datetime

from src.hexagonal.video.domain.vo.id import VideoId
from src.hexagonal.video.domain.vo.title import VideoTitle
from src.hexagonal.video.domain.vo.duration import VideoDuration
from src.hexagonal.video.domain.vo.category import VideoCategory
from src.hexagonal.video.domain.vo.updated import VideoUpdated
from src.hexagonal.shared.domain.user.vo.id import UserId


class Video:
    __slots__ = ('id', 'title', 'duration_in_seconds', 'category', 'creator_id', 'updated_at',)

    def __init__(self, id: VideoId, title: VideoTitle, duration_in_seconds: VideoDuration, category: VideoCategory,
                 creator_id: UserId, updated_at: VideoUpdated = None):
        self.id = id
        self.title = title
        self.duration_in_seconds = duration_in_seconds
        self.category = category
        self.creator_id = creator_id
        self.updated_at = updated_at if updated_at else VideoUpdated(datetime.now())

    @staticmethod
    def create(id: VideoId, title: VideoTitle, duration_in_seconds: VideoDuration, category: VideoCategory,
               creator_id: UserId) -> Video:
        video = Video(id, title, duration_in_seconds, category, creator_id)
        return video
