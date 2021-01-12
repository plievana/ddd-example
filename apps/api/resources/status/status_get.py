from apps.api.resources import Resource
from src.hexagonal.status.application.status_getter import StatusGetter


class StatusResource(Resource):
    def get(self):
        return StatusGetter().get()
