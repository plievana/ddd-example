import abc


class ValueObject(abc.ABC):

    def __init__(self, value):
        self.__class__._validate(value)
        self._value = value

    @classmethod
    @abc.abstractmethod
    def _validate(cls, value):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def _raise_validation_exception(cls, value):
        raise NotImplementedError

    @property
    def native(self):
        return self.value

    @property
    def value(self):
        return self._value
