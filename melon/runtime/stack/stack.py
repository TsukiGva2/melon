# TODO

from collections import deque
from itertools import repeat
from queue import LifoQueue

from melon.helpers.function import apply


# printable, easier to debug
class DequeStack:
    def __init__(self):
        self.deque = deque([])

    def get(self):
        return self.deque.pop()

    def put(self, n):
        return self.deque.append(n)

    def printable(self):
        return f"({' '.join(map(str,self.deque))})"


# not printable, harder to debug, but good for concurrency
class QueueStack(LifoQueue):
    def printable(self):  # TODO
        return "( Queue )"


class Stack:
    def __init__(self):
        # self.backend = QueueStack()
        self.backend = DequeStack()

    def __iter__(self):
        return iter(self.backend.get, None)

    def inspect(self):
        print(self.backend.printable())

    def put(self, entries):
        for entry in entries:
            self.backend.put(entry)

    def ask(self, n):
        if n <= 0:
            return iter([])

        return map(apply, repeat(self.backend.get, n))
