from http import HTTPStatus
from flask import request

from apps.api.resources import Resource
from src.hexagonal.video.domain.vo.id import VideoId
from src.hexagonal.video.domain.vo.title import VideoTitle
from src.hexagonal.video.domain.vo.duration import VideoDuration
from src.hexagonal.video.domain.vo.category import VideoCategory
from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.video.application.video_creator import VideoCreator


class VideosPostResource(Resource):

    def post(self):
        data = request.json
        id = data.get('id')
        title = data.get('title')
        duration_in_seconds = data.get('duration_in_seconds')
        category = data.get('category')
        creator_id = data.get('creator_id')

        VideoCreator.create(id=VideoId.from_text(id),
                            title=VideoTitle.from_text(title),
                            duration_in_seconds=VideoDuration.from_text(duration_in_seconds),
                            category=VideoCategory.from_text(category),
                            creator_id=UserId.from_text(creator_id))

        return '', HTTPStatus.NO_CONTENT
