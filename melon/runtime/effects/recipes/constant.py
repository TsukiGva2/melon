from .recipe import Recipe


class Constant(Recipe):
    def __call__(self, _):
        return (self.function(),)