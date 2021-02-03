from .resources.status.status_get import StatusResource
from .resources.users.users_get import UsersGetResource
from .resources.users.users_post import UsersPostResource
from .resources.user.user_delete import UserDeleteResource
from .resources.videos.videos_get import VideosGetResource
from .resources.videos.videos_post import VideosPostResource
from .resources.video.video_delete import VideoDeleteResource


def register_routes(api):
    api.add_resource(StatusResource, '/status')
    api.add_resource(VideosGetResource, '/videos')
    api.add_resource(VideosPostResource, '/videos')
    api.add_resource(VideoDeleteResource, '/video/<id>')
    api.add_resource(UsersGetResource, '/users')
    api.add_resource(UsersPostResource, '/users')
    api.add_resource(UserDeleteResource, '/user/<id>')
