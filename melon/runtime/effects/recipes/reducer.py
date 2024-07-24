from functools import reduce

from .recipe import Recipe


class Reducer(Recipe):
    def __call__(self, entries):
        return reduce(self.function, entries)
