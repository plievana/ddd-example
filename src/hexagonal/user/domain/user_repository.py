import abc
from typing import Sequence
from src.hexagonal.user.domain.user import User


class UserRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def all(self) -> Sequence[User]:
        raise NotImplementedError

    @abc.abstractmethod
    def save(self, user: User) -> None:
        raise NotImplementedError
