# from collections import OrderedDict

from .errors import Melon_EffectsStorageResolveError


class EffectStorage:
    def __init__(self, global_dict):
        self.global_dict = global_dict
        self.local_dict = dict()

    def derive(self):
        """
        Create a new EffectStorage with locals+globals as the
        global dict. Essentially passing all of the definitions
        to the new storage object.
        """
        return EffectStorage((self.local_dict | self.global_dict))

    def resolve(self, strWord):
        try:
            return (self.local_dict | self.global_dict)[strWord]
        except IndexError:
            raise Melon_EffectsStorageResolveError(f"No such word: {strWord}")
