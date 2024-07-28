# from collections import deque
from enum import Enum

EntryType = Enum("EntryType", ["IN", "OUT"])


class EntryLog:
    def __init__(self):
        self.counts = {EntryType.IN: 0, EntryType.OUT: 0}
        self.output = ()

    def increment(self, entry_type, n=1):
        self.counts[entry_type] += n

    def annotate(self):
        inputs = " ".join(["n"] * self.counts[EntryType.IN])

        # 1 output = 1 x all entries
        output = " ".join(
            ["n"] * (self.counts[EntryType.OUT] * self.counts[EntryType.IN])
        )

        return f"\tIn: ({inputs}) -> Out: ({output})"

    def out(self, output):
        self.output = output

    def count_outputs(self):
        return self.counts[EntryType.OUT]

    def count_inputs(self):
        return self.counts[EntryType.IN]
