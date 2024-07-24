from functools import partial

from melon.runtime.fun.builtins.builtins import Melon_fetch


class Word:
    def __init__(self, token):
        self.token = token
        self.compiled = partial(Melon_fetch, self.token)

    def __call__(self, state):
        return self.compiled(state)
