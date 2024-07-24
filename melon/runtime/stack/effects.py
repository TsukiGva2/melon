# TODO: stack transformation checking

from collections import deque, namedtuple

from .errors import InvalidFragment


def apply(f):
    return f()


Fragment = namedtuple("Fragment", ["WILDCARD", "MAP", "FETCH", "IN", "OUT"])


class Effect:
    def __init__(self):
        self.fragments = deque([])
        self.entries = []  # Inputs + Fetches
        self.outputs = []

    def input(self):
        """
        Get entry from runtime (stack)
        """
        self.fragments.appendleft(Fragment.IN)

    def map(self):
        """
        Apply a Fetched Effect in entries to all entries
        """
        self.fragments.appendleft(Fragment.MAP)

    def output(self):
        """
        Insert an entry into the runtime (stack)
        """
        self.fragments.appendleft(Fragment.OUT)

    def fetch(self):
        """
        Fetch an Effect to the entry list
        """
        self.fragments.appendleft(Fragment.FETCH)

    def apply(self, runtime):
        self.entries = runtime.ask(self.fragments.count(Fragment.IN))
