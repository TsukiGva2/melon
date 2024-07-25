from functools import partial

from .recipe import Recipe


def view(function, entry):
    function(entry)

    return entry


class Viewer(Recipe):
    def __call__(self, entries):
        return map(partial(view, self.function), entries)
