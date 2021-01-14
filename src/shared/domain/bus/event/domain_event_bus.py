import abc
from typing import Sequence

from src.shared.domain.bus.event.domain_event import DomainEvent


class DomainEventBus(abc.ABC):

    @abc.abstractmethod
    def publish(self, events: Sequence[DomainEvent]) -> None:
        raise NotImplementedError
