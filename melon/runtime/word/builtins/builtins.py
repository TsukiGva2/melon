import melon.runtime.stack.effects as stack_effects
from melon.runtime.doc.doc import Doc


# ( Quote -- Doc )
@stack_effects.N_N
def help(n):
    return Doc(n)
