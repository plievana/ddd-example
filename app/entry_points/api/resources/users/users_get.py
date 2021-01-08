from app.entry_points.api.resources import Resource


class UsersGetResource(Resource):

    def __init__(self, **kwargs):
        self.users_searcher = kwargs.get('users_searcher')

    def get(self):
        return self.users_searcher.all()
