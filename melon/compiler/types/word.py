from melon.runtime.effects.effects import Effect
from melon.runtime.library.builtins.builtins import Melon_fetch


def Word(token) -> Effect:
    return Melon_fetch(token)
