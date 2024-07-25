from melon.runtime.effects.storage import EffectStorage
from melon.runtime.stack.stack import Stack


class Runtime:
    def __init__(self):
        self.effects = EffectStorage()
        self.stacker = Stack()

    # .ASK, .RESOLVE
    def __getattr__(self, attr):
        match attr.upper():
            case "ASK" | "PUT":
                return getattr(self.stacker, attr)
            case "RESOLVE" | "SAVE":
                return getattr(self.effects, attr)
            case _:
                raise AttributeError(f"No such method: {attr}")

    def next(self):
        return next(self.compilation_stream)

    def execute(self, compstream):
        self.compilation_stream = compstream

        for effect in self.compilation_stream:
            effect.apply(self)
