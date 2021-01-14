from typing import Sequence

from src.shared.domain.bus.event.domain_event import DomainEvent


class AggregateRoot:
    __slots__ = ('_domain_events',)

    def __init__(self):
        self._domain_events = []

    def _record(self, domain_event: DomainEvent) -> None:
        self._domain_events.append(domain_event)

    def pull_domain_events(self) -> Sequence[DomainEvent]:
        domain_events = self._domain_events
        self._domain_events = []
        return domain_events
