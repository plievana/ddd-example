import inspect
import random

from src.shared.domain.vo.enum import REGEX


class EnumMother:

    @classmethod
    def create(cls) -> str:
        opts = []
        for k, v in inspect.getmembers(cls):
            if not REGEX.match(k) and not callable(v):
                opts.append(v)

        return random.choice(opts)
