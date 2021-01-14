import abc
from typing import Sequence


class DomainEventSubscriber(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def subscribed_to(cls) -> Sequence:
        raise NotImplementedError
