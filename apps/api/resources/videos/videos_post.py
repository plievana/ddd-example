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
        duration_in_seconds = int(data.get('duration_in_seconds'))
        category = data.get('category')
        creator_id = data.get('creator_id')

        VideoCreator.create(id=VideoId(id),
                            title=VideoTitle(title),
                            duration_in_seconds=VideoDuration(duration_in_seconds),
                            category=VideoCategory(category),
                            creator_id=UserId(creator_id))

        return '', HTTPStatus.NO_CONTENT
