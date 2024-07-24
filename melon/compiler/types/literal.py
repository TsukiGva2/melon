from functools import partial

from melon.runtime.fun.builtins.builtins import Melon_LIT


class Literal:
    def __init__(self, token):
        self.value = token
        self.compiled = partial(Melon_LIT, self.value)

    def __call__(self, state):
        return self.compiled(state)
