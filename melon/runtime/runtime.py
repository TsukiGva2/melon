from melon.runtime.effects.context import EffectContext
from melon.runtime.effects.storage import EffectStorage
from melon.runtime.modes import RuntimeMode
from melon.runtime.stack.stack import Stack


class Runtime:
    def __init__(self):
        self.effects = EffectStorage()
        self.stacker = Stack()

        self.runmode = RuntimeMode.IMMEDIATE

        self.mainctx = EffectContext(name="main", mode=self.runmode)
        self.mainctx.resolver(self.effects)
        self.mainctx.input(self.stacker)

    def next(self):
        return next(self.compilation_stream)

    def execute(self, compstream):
        self.compilation_stream = compstream

        for effect in self.compilation_stream:
            with self.mainctx as ctx:
                effect.apply(ctx)
