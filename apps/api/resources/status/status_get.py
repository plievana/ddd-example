from apps.api.resources import Resource


class StatusResource(Resource):
    def __init__(self, **kwargs):
        self.status_getter = kwargs.get('status_getter')

    def get(self):
        return self.status_getter.get()
