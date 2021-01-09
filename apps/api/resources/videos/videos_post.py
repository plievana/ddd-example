from http import HTTPStatus
from flask import request

from apps.api.resources import Resource


class VideosPostResource(Resource):

    def __init__(self, **kwargs):
        self.videos_creator = kwargs['videos_creator']

    def post(self):
        data = request.json
        id = data.get('id')
        title = data.get('title')
        duration_in_seconds = int(data.get('duration_in_seconds'))
        category = data.get('category')
        creator_id = data.get('creator_id')
        self.videos_creator.create(id=id, title=title, duration_in_seconds=duration_in_seconds, category=category, creator_id=creator_id)
        return '', HTTPStatus.NO_CONTENT
