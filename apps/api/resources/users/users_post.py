from http import HTTPStatus
from flask import request

from apps.api.resources import Resource

from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.user.domain.vo.name import UserName
from src.hexagonal.user.application.user_creator import UserCreator


class UsersPostResource(Resource):

    def post(self):
        data = request.json
        id = data.get('id')
        name = data.get('name')

        UserCreator.create(id=UserId(id), name=UserName(name))

        return '', HTTPStatus.NO_CONTENT
