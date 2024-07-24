import melon.runtime.stack.effects as effects
from melon.runtime.doc.doc import docs

# Exposed functions


# Eff: ( Quote -- Doc )
def help_word() -> effects.Effect:
    return effects.Effect().input().map(docs)


# Special functions, "Melon_" prefixed


# Eff: ( -- literal ) _Takes: n
def Melon_LIT(n) -> effects.Effects:
    return effects.Effect().output(n)


# Eff: ( -- ) _Fetches: strWord
def Melon_fetch(strWord) -> effects.Effect:
    return effects.Effect().fetch(strWord)


# Exposing non-special functions

MelonBuiltins = {"help": help_word}
