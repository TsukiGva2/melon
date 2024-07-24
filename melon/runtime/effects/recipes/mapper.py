from .recipe import Recipe


class Mapper(Recipe):
    def __call__(self, entries):
        return map(self.function, entries)
