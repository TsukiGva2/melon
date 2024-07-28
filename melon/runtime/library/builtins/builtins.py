import melon.runtime.effects.effects as effects
from melon.runtime.library.doc.doc import getDoc
from melon.runtime.library.io.io import show

# Exposed functions

help_word = effects.Effect().input() >> getDoc
show_word = effects.Effect().input() >> show

MelonBuiltins = {"help": help_word, "show": show_word}
