from http import HTTPStatus

from apps.api.resources import Resource
from src.hexagonal.video.domain.vo.id import VideoId
from src.hexagonal.video.application.delete.video_deleter import VideoDeleter


class VideoDeleteResource(Resource):

    def delete(self, id):
        VideoDeleter.delete(VideoId.from_text(id))
        return '', HTTPStatus.NO_CONTENT
