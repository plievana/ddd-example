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

        try:
            UserId.from_text(id)
        except Exception as e:
            from flask import current_app
            current_app.logger.error(str(e), exc_info=True)

        UserCreator.create(id=UserId.from_text(id), name=UserName.from_text(name))

        return '', HTTPStatus.NO_CONTENT
