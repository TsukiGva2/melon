from .recipe import Recipe


class Filter(Recipe):
    def __call__(self, entries):
        return filter(self.function, entries)
