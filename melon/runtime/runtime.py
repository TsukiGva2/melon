from runtime.effects.storage import EffectStorage
from runtime.stack.stack import Stack


class Runtime:
    def __init__(self):
        self.effects = EffectStorage()
        self.stacker = Stack()

    # .ASK, .RESOLVE
    def __getattr__(self, attr):
        match attr.upper():
            case "ASK":
                return self.stacker.ask
            case "RESOLVE":
                return self.effects.resolve
            case _:
                raise AttributeError(f"No such method: {attr}")

    def execute(self, compstream):
        for effect in compstream:
            effect.apply(self.stack)
