from app.api import resources
from .resources.status import StatusResource
from .resources.users import UsersResource
from .resources.videos import VideosResource


def register_endpoints(api):
    api.add_resource(StatusResource, '/status')
    api.add_resource(VideosResource, '/videos')
    api.add_resource(UsersResource, '/users')