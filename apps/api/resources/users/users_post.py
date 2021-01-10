from http import HTTPStatus
from flask import request

from apps.api.resources import Resource

from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.user.domain.vo.name import UserName


class UsersPostResource(Resource):

    def __init__(self, **kwargs):
        self.users_creator = kwargs['users_creator']

    def post(self):
        data = request.json
        id = data.get('id')
        name = data.get('name')

        self.users_creator.create(id=UserId(id), name=UserName(name))

        return '', HTTPStatus.NO_CONTENT
