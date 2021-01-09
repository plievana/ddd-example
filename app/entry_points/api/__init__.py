from flask import Blueprint, Config
from flask_restful import Api

from src.shared.infrastructure.mongo_connection import MongoDB
from src.hexagonal.user.infrastructure.dependency_injection import UserModuleDependencyContainer
from .api_dependency_container import ApiDependencyContainer
from src.hexagonal.status.infrastructure.dependency_injection import StatusModuleDependencyContainer
from src.hexagonal.video.infrastructure.dependency_injection import VideoModuleDependencyContainer


def create_blueprint(config: Config):
    bp = Blueprint('api', __name__)
    api = Api(bp)

    db_connection = MongoDB(host=config.get('MONGO_HOST'),
                            port=config.get('MONGO_PORT'),
                            db=config.get('MONGO_DB'),
                            user=config.get('MONGO_USER'),
                            password=config.get('MONGO_PASSWORD'))

    user_dependencies = UserModuleDependencyContainer(db_connection)
    video_dependencies = VideoModuleDependencyContainer(db_connection)
    status_dependencies = StatusModuleDependencyContainer()
    api_dependencies = ApiDependencyContainer(user_dependencies, video_dependencies, status_dependencies)

    from .routes import register_routes
    register_routes(api, api_dependencies)

    return bp
