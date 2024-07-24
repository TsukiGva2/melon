import melon.runtime.stack.effects as effects
from melon.runtime.library.doc.doc import getDoc

# Exposed functions


# Eff: ( Quote -- Doc )
def help_word() -> effects.Effect:
    return effects.Effect().input() | getDoc


# Special functions, "Melon_" prefixed


# Eff: ( -- literal ) _Takes: n
def Melon_LIT(n) -> effects.Effects:
    return effects.literal(n)


# Eff: ( -- ) _Fetches: strWord
def Melon_fetch(strWord) -> effects.Effect:
    return effects.fetch(strWord)


# Exposing non-special functions

MelonBuiltins = {"help": help_word}
