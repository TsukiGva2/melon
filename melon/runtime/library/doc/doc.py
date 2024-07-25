from melon.runtime.effects.effects import Effect
from melon.runtime.effects.recipes.mapper import Mapper


def document(eff: Effect):
    return eff.

Doc: Mapper = Mapper(document)
getDoc: Effect = Effect() >> Doc
