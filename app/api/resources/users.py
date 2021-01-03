from http import HTTPStatus
from flask import request

from app.repositories.user_repository import UserRepository
from app.models.user import User
from . import Resource


class UsersResource(Resource):

    def get(self):
        return UserRepository().all()

    def post(self):
        user = User().load(request.json)
        UserRepository().save(user)
        return '', HTTPStatus.NO_CONTENT
