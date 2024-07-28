# from itertools import chain
from melon.runtime.effects.context import EffectContext
from melon.runtime.effects.storage import EffectStorage
from melon.runtime.library.builtins.builtins import MelonBuiltins
from melon.runtime.modes import RuntimeMode
from melon.runtime.stack.stack import Stack


class Runtime:
    def __init__(self):
        self.stack = Stack()

        self.scope = EffectStorage(MelonBuiltins)

        self.ctx = EffectContext(
            inputs=iter(self.stack),
            scope=self.scope,
            output=self.stack,
            name="main",
            mode=RuntimeMode.IMMEDIATE,
        )

    def next(self):
        return next(self.compilation_stream)

    def execute(self, compstream):
        self.compilation_stream = compstream

        for effect in self.compilation_stream:
            with self.ctx as ctx:
                ctx.apply(effect)
