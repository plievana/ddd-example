import random
import sys

class IntegerMother:

    @classmethod
    def create(cls):
        return cls.between(1)

    @classmethod
    def between(cls, min: int, max: int = None) -> int:
        max = sys.maxsize if max is None else max
        return random.randint(min, max)

    @classmethod
    def less_than(cls, max: int) -> int:
        return cls.between(1, max)
