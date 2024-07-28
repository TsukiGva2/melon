from melon.runtime.effects.effects import Effect
from melon.runtime.effects.recipes.mapper import Mapper


def document(eff: Effect) -> str:
    return eff.docs


getDoc: Mapper = Mapper(document)
