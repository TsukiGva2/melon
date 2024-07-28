# TODO

from itertools import repeat
from queue import LifoQueue

from melon.helpers.function import apply


class Stack:
    def __init__(self):
        self.stack = LifoQueue()

    def __iter__(self):
        yield self.stack.get()

    def put(self, entries):
        for entry in entries:
            self.stack.put(entry)

    def ask(self, n):
        if n <= 0:
            return iter([])

        return map(apply, repeat(self.stack.get, n))
