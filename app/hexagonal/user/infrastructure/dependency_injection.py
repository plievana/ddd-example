from app.hexagonal.shared.infrastructure.db_connection import DBConnection
from app.hexagonal.user.domain.user_repository import UserRepository
from app.hexagonal.user.infrastructure.repository.mongo_user_repository import MongoUserRepository
from app.hexagonal.user.application.user_searcher import UserSearcher
from app.hexagonal.user.application.user_creator import UserCreator


class UserModuleDependencyContainer:
    __slots__ = ('db_connection',)

    def __init__(self, db_connection: DBConnection):
        self.db_connection = db_connection

    @property
    def _repository(self) -> UserRepository:
        return MongoUserRepository(self.db_connection)

    @property
    def user_searcher(self) -> UserSearcher:
        return UserSearcher(self._repository)

    @property
    def user_creator(self) -> UserCreator:
        return UserCreator(self._repository)
