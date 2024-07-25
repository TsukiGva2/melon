from collections import OrderedDict

from runtime.word.builtins.builtins import MelonBuiltins

from .errors import Melon_EffectsStorageResolveError


class EffectStorage:
    def __init__(self):
        self.dict: OrderedDict = OrderedDict(MelonBuiltins)

    def resolve(self, strWord):
        try:
            return self.dict[strWord]
        except IndexError:
            raise Melon_EffectsStorageResolveError(f"No such word: {strWord}")
