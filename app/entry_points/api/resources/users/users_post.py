from http import HTTPStatus
from flask import request

from app.entry_points.api.resources import Resource


class UsersPostResource(Resource):

    def __init__(self, **kwargs):
        self.users_creator = kwargs['users_creator']

    def post(self):
        data = request.json
        id = data.get('id')
        name = data.get('name')
        self.users_creator.create(id=id, name=name)
        return '', HTTPStatus.NO_CONTENT
