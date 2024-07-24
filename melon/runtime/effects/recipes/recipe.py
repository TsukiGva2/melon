from typing import final


class Recipe:
    @final
    def __init__(self, f):
        self.function = f

    def __call__(self, entries): ...
