import melon.runtime.effects.effects as effects
from melon.runtime.library.doc.doc import getDoc
from melon.runtime.library.io.io import read, show

# Exposed functions

help_word = effects.Effect().input() >> getDoc
show_word = effects.Effect().input() >> show
read_word = effects.Effect() >> read

MelonBuiltins = {"help": help_word, "show": show_word, "read": read_word}
