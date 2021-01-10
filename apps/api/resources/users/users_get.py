from apps.api.resources import Resource
from apps.api.encoders.user import UserEncoder


class UsersGetResource(Resource):

    def __init__(self, **kwargs):
        self.users_searcher = kwargs.get('users_searcher')

    def get(self):
        return [UserEncoder.encode(u) for u in self.users_searcher.all()]
