from itertools import chain, islice

from melon.runtime.modes import RuntimeMode

from .entrylog import EntryLog, EntryType
from .errors import Melon_EffectContextNoRuntimeError


class EffectContext:
    def __init__(
        self, parent=None, mode=RuntimeMode.IMMEDIATE, name="anon", child=False
    ):
        self.inputs = iter([])
        self.outputs = iter([])

        self.mode = mode
        self.name = name

        self.is_child = child

        self.entrylog = EntryLog()

    def __getattribute__(self):
        if self.runtime is None:
            raise Melon_EffectContextNoRuntimeError

        return object.__getattribute__(self)

    def annotate(self):
        print(f"{self.entrylog.annotate()}\n")

    def input(self, inputs):
        self.inputs = inputs

    def output(self, entries):
        output = list(entries)

        self.entrylog.out(output)

        self.put(output)

    def ask(self, count):
        self.entrylog.increment(EntryType.IN)

        return islice(self.inputs, count)

    def put(self, entries):
        if self.is_child:
            self.outputs = chain(entries, self.outputs)
            return self.outputs

        return self.runtime.stacker.put(*entries)

    # .ASK, .RESOLVE
    def __getattr__(self, attr):
        match attr.upper():
            case "RESOLVE" | "SAVE":
                return getattr(self.runtime.effects, attr)
            case _:
                return getattr(self.runtime, attr)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        # self.annotate()
        # print(f"Leaving {self.name}...")
        pass
