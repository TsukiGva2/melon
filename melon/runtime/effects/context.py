from melon.runtime.modes import RuntimeMode


class EffectContext:
    def __init__(self, runtime, mode=RuntimeMode.IMMEDIATE, name="anon"):
        self.mode = mode
        self.name = name

        self.runtime = runtime

    # .ASK, .RESOLVE
    def __getattr__(self, attr):
        match attr.upper():
            case "ASK" | "PUT":
                return getattr(self.runtime.stacker, attr)
            case "RESOLVE" | "SAVE":
                return getattr(self.runtime.effects, attr)
            case _:
                raise AttributeError(f"No such method: {attr}")

    def __enter__(self):
        return self

    def __exit__(self): ...
