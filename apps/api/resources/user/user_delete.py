from http import HTTPStatus

from apps.api.resources import Resource
from src.hexagonal.shared.domain.user.vo.id import UserId
from src.hexagonal.user.application.user_deleter import UserDeleter


class UserDeleteResource(Resource):

    def delete(self, id):
        UserDeleter.delete(UserId.from_text(id))
        return '', HTTPStatus.NO_CONTENT
