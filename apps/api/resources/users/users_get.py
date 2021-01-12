from apps.api.resources import Resource
from apps.api.encoders.user import UserEncoder
from src.hexagonal.user.application.user_searcher import UserSearcher


class UsersGetResource(Resource):

    def get(self):
        return [UserEncoder.encode(u) for u in UserSearcher.all()]
