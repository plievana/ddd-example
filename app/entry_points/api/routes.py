from . import ApiDependencyContainer
from .resources.status.status_get import StatusResource
from .resources.users.users_get import UsersGetResource
from .resources.users.users_post import UsersPostResource
from .resources.videos.videos_get import VideosGetResource
from .resources.videos.videos_post import VideosPostResource


def register_routes(api, api_dependencies: ApiDependencyContainer):
    api.add_resource(StatusResource, '/status', resource_class_kwargs={'status_getter': api_dependencies.status_dependencies.status_getter})
    api.add_resource(VideosGetResource, '/videos', resource_class_kwargs={'videos_searcher': api_dependencies.video_dependencies.video_searcher})
    api.add_resource(VideosPostResource, '/videos', resource_class_kwargs={'videos_creator': api_dependencies.video_dependencies.video_creator})
    api.add_resource(UsersGetResource, '/users', resource_class_kwargs={'users_searcher': api_dependencies.user_dependencies.user_searcher})
    api.add_resource(UsersPostResource, '/users', resource_class_kwargs={'users_creator': api_dependencies.user_dependencies.user_creator})
