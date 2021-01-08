from app.hexagonal.status.infrastructure.dependency_injection import StatusModuleDependencyContainer
from app.hexagonal.user.infrastructure.dependency_injection import UserModuleDependencyContainer
from app.hexagonal.video.infrastructure.dependency_injection import VideoModuleDependencyContainer


class ApiDependencyContainer:
    __slots__ = ('user_dependencies', 'video_dependencies', 'status_dependencies')

    def __init__(self,
                 user_dependencies: UserModuleDependencyContainer,
                 video_dependencies: VideoModuleDependencyContainer,
                 status_dependencies: StatusModuleDependencyContainer):
        self.user_dependencies = user_dependencies
        self.video_dependencies = video_dependencies
        self.status_dependencies = status_dependencies

    @property
    def users_searcher(self):
        return self.user_dependencies.user_searcher

    @property
    def users_creator(self):
        return self.user_dependencies.user_creator

    @property
    def video_searcher(self):
        return self.video_dependencies.video_searcher

    @property
    def video_creator(self):
        return self.video_dependencies.video_creator

    @property
    def status_getter(self):
        return self.status_dependencies.status_getter


