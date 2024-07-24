import melon.runtime.stack.effects as effects
from melon.runtime.doc.doc import docs

# Exposed functions


# Eff: ( Quote -- Doc )
@effects.effect("n", True)
def help_word(n):
    return docs(n)


# Special functions, "Melon_" prefixed


# Eff: ( -- literal ) _Takes: n
@effects.
def Melon_LIT(n):
    return n


# Eff: ( -- ) _Fetches: strWord
@effects.effect("...", False)
def Melon_fetch(f, state):
    return f(state)


# Exposing non-special functions

MelonBuiltins = {"help": help_word}
