from melon.runtime.effects.effects import Effect
from melon.runtime.library.builtins.builtins import Melon_LIT


def Literal(value) -> Effect:
    return Melon_LIT(value)
