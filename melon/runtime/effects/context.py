from itertools import chain, islice

from melon.runtime.modes import RuntimeMode

from .entrylog import EntryLog, EntryType

# from .storage import EffectStorage

# from .errors import Melon_EffectContextNoRuntimeError


class EffectContext:
    def __init__(self, inputs, scope, mode=RuntimeMode.IMMEDIATE, name="anon"):
        self.inputs = inputs
        self.outputs = iter([])
        self.entrylog = EntryLog()

        self.scope = scope.derive()

        self.mode = mode
        self.name = name

    # def annotate(self):
    #   print(f"{self.entrylog.annotate()}\n")

    def resolve(self, strWord):
        return self.scope.resolve(strWord)

    def put(self, entries):
        self.outputs = chain(entries, self.outputs)

    def output(self, entries):
        # output = list(entries)
        self.entrylog.increment(EntryType.OUT)
        self.put(entries)

    def ask(self, count):
        self.entrylog.increment(EntryType.IN)
        return islice(self.inputs, count)
