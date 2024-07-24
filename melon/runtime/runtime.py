from collections import OrderedDict

from runtime.word.builtins.builtins import MelonBuiltins


class Runtime:
    def __init__(self):
        self.effects = OrderedDict(MelonBuiltins)

    def execute(self):
        return
