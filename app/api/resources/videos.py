from http import HTTPStatus
from flask import request

from app.repositories.video_repository import VideoRepository
from app.models.video import Video
from . import Resource


class VideosResource(Resource):

    def get(self):
        return VideoRepository().all()

    def post(self):
        video = Video().load(request.json)
        VideoRepository().save(video)
        return '', HTTPStatus.NO_CONTENT
