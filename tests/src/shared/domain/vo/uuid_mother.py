import uuid


class UuidMother:

    @classmethod
    def create(cls) -> uuid.UUID:
        return uuid.uuid4()
