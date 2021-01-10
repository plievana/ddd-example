from src.hexagonal.video.domain.video import Video


class VideoEncoder(list):
    @staticmethod
    def encode(video: Video) -> dict:
        return {
            'id': video.id.native,
            'title': video.title.native,
            'duration_in_seconds': video.duration_in_seconds.native,
            'category': video.category.native,
            'creator_id': video.creator_id.native,
            'updated_at': video.updated_at.native
        }
