from . import Resource


class StatusResource(Resource):
    def get(self):
        return {'status': 'ok'}
