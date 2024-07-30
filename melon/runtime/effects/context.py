from itertools import chain, islice

from melon.runtime.modes import RuntimeMode

from .entrylog import EntryLog, EntryType

# from .storage import EffectStorage

# from .errors import Melon_EffectContextNoRuntimeError


class EffectContext:
    def __init__(
        self, scope, output_buffer=None, mode=RuntimeMode.IMMEDIATE, name="anon"
    ):
        self.inputs = iter([])
        self.outputs = iter([])

        self.entrylog = EntryLog()

        self.scope = scope.derive()

        self.output_buffer = output_buffer

        self.mode = mode

        self.name = name

    def annotate(self):
        print(f"{self.entrylog.annotate()}\n")

    def resolve(self, strWord):
        return self.scope.resolve(strWord)

    def put(self, entries):
        self.outputs = chain(entries, self.outputs)

    def output(self, entries):
        # output = list(entries)
        self.entrylog.increment(EntryType.OUT)
        self.put(entries)

    def set_inputs(self, inputs, fallback=[]):
        self.inputs = chain(inputs, fallback)

    def ask(self, count):
        self.entrylog.increment(EntryType.IN)
        return islice(self.inputs, count)

    def apply(self, effect):
        effect.apply(self)
        return self.outputs

    def __enter__(self):
        return self

    # TODO: error handling
    def __exit__(self, *exc):
        if self.output_buffer is not None:
            self.output_buffer.put(self.outputs)

        self.annotate()
        self.entrylog.reset()
