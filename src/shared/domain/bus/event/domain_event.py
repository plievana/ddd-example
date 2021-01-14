from __future__ import annotations
import uuid
import abc
from datetime import datetime

from src.shared.domain.utils import Utils


class DomainEvent(abc.ABC):
    event_name: str = NotImplementedError

    def __init__(self, id: str, event_id: str = None, occurred_on: str = None):
        self.id = id
        self.event_id = event_id if event_id else uuid.uuid4()
        self.occurred_on = occurred_on if occurred_on else Utils.date_to_str(datetime.now())

    @classmethod
    @abc.abstractmethod
    def from_primitives(cls, id: str, body: dict, event_id: str, occurred_on: str) -> DomainEvent:
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def to_primitives(cls) -> dict:
        raise NotImplementedError
