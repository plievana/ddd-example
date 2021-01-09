from src.hexagonal.status.application.status_getter import StatusGetter


class StatusModuleDependencyContainer:
    def __init__(self):
        pass

    @property
    def status_getter(self) -> StatusGetter:
        return StatusGetter()
