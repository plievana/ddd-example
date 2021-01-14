from blinker import signal
from typing import Sequence

from src.shared.domain.bus.event.domain_event import DomainEvent
from src.shared.domain.bus.event.domain_event_bus import DomainEventBus


class BlinkerDomainEventBus(DomainEventBus):
    def publish(self, events: Sequence[DomainEvent]) -> None:
        for event in events:
            s = signal(event.event_name)
            if bool(s.receivers):
                s.send(event)

