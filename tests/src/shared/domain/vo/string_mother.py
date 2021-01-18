import random
import string

letters = string.ascii_letters


class StringMother:

    @classmethod
    def create(cls) -> str:
        return cls.of_length(10)

    @classmethod
    def of_length(cls, length: int) -> str:
        return ''.join(random.choice(letters) for _ in range(length))
