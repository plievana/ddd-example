from src.shared.domain.bus.event.domain_event import DomainEvent


class UserCreatedDomainEvent(DomainEvent):
    event_name = 'user.created'

    def __init__(self, id: str, name: str, event_id: str = None, occurred_on: str = None):
        self.name = name
        super(UserCreatedDomainEvent, self).__init__(id, event_id, occurred_on)

    @classmethod
    def from_primitives(cls, id: str, body: dict, event_id: str, occurred_on: str) -> DomainEvent:
        return UserCreatedDomainEvent(id, body['name'], event_id, occurred_on)

    def to_primitives(self) -> dict:
        return {
            'name': self.name
        }
