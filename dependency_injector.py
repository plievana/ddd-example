import inject
from flask import Flask

from src.hexagonal.user.domain.user_repository import UserRepository
from src.hexagonal.user.infrastructure.repository.mongo_user_repository import MongoUserRepository
from src.hexagonal.video.domain.video_repository import VideoRepository
from src.hexagonal.video.infrastructure.repository.mongo_video_repository import MongoVideoRepository
from src.shared.infrastructure.db_connection import DBConnection
from src.shared.infrastructure.mongo_connection import MongoDB


def di_configuration(binder, app: Flask):
    mongo_db = MongoDB(host=app.config.get('MONGO_HOST'),
                       port=app.config.get('MONGO_PORT'),
                       db=app.config.get('MONGO_DB'),
                       user=app.config.get('MONGO_USER'),
                       password=app.config.get('MONGO_PASSWORD'))
    binder.bind(DBConnection, mongo_db)
    binder.bind(MongoDB, mongo_db)
    binder.bind(UserRepository, MongoUserRepository(mongo_db))
    binder.bind(VideoRepository, MongoVideoRepository(mongo_db))


def load_dependencies(app: Flask):
    inject.configure(lambda binder: di_configuration(binder, app))
