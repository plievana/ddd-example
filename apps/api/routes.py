from .resources.status.status_get import StatusResource
from .resources.users.users_get import UsersGetResource
from .resources.users.users_post import UsersPostResource
from .resources.videos.videos_get import VideosGetResource
from .resources.videos.videos_post import VideosPostResource


def register_routes(api):
    api.add_resource(StatusResource, '/status')
    api.add_resource(VideosGetResource, '/videos')
    api.add_resource(VideosPostResource, '/videos')
    api.add_resource(UsersGetResource, '/users')
    api.add_resource(UsersPostResource, '/users')
