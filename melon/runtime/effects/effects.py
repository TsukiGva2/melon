# TODO: stack transformation checking

from collections import deque, namedtuple

from melon.helpers import popper

from .recipes.default import Literal
from .recipes.recipe import Recipe

# from .errors import InvalidFragment

Fragment = namedtuple("Fragment", ["MAP", "FETCH", "IN", "OUT", "APPLY"])

# helpers


def apply(f):
    return f()


def cancel_outputs(f: Fragment):
    return f != Fragment.OUT


# definitions


class Effect:
    def __init__(self, fragments=deque([]), recipes=deque([])):
        self.fragments = fragments

        self.recipes = recipes  # Reducers, Mappers and Filters
        self.outputs = None

    def __or__(self, effect):
        if not isinstance(effect, Effect):
            raise TypeError("Can't join effect with non-effect")

        # appendleft(effects.fragments)
        return Effect(effect.fragments + filter(cancel_outputs, self.fragments))

    def __rshift__(self, recipe: Recipe):
        if not isinstance(recipe, Recipe):
            raise TypeError("Can't apply non-recipe to Effect entries")

        return Effect(self.fragments, self.recipes)

    def input(self):
        """
        Get entry from runtime (stack)
        """
        self.fragments.appendleft(Fragment.IN)

    def map(self):
        """
        Apply a Fetched Effect in entries using entries as input
        """
        self.fragments.appendleft(Fragment.MAP)

    def output(self):
        """
        Insert an entry into the runtime (stack)
        """
        self.fragments.appendleft(Fragment.OUT)

    def fetch(self):
        """
        Fetch an Effect from an entry to the entry list
        """
        self.fragments.appendleft(Fragment.FETCH)

    def recipe(self, r: Recipe):
        self.recipes.appendleft(r)
        self.fragments.appendleft(Fragment.APPLY)

    def apply(self, runtime):
        """
        1. recursively resolve fragments

            1.1. inputs
                Example:

                    Suppose we did:
                        effects.literal ( 'stack 'im 'a 'hey )

                    [0] 'hey
                    [1] 'im
                    [2] 'a
                    [3] 'stack

                                       (slice?)
                    Runtime.ask (4) ->   pop + appendleft x4 -> deque [ 'stack 'a 'im 'hey ]

                    entries <- deque [ 'stack 'a 'im 'hey ]
        """

        # Fetches + Inputs
        entries = runtime.ask(self.fragments.count(Fragment.IN))

        def resolve_inputs(fragments):
            entries.extendleft(runtime.ask(fragments.count(Fragment.IN)))

        def resolve_recipes(new_recipes):
            self.recipes = new_recipes + self.recipes

        def resolve_effect():
            effect = runtime.resolve(popper(entries))

            # applies come automatically with the fragments
            resolve_recipes(effect.recipes)

            fragments = effect.fragments
            resolve_inputs(fragments)

            return fragments

        def fetch(fragments):
            match fragments:
                case []:
                    yield []
                case [Fragment.FETCH, *tail]:
                    yield from fetch(resolve_effect() + tail)
                case [_, *tail]:
                    yield from fetch(tail)

        fragments = fetch(self.fragments)

        print(
            f"result: f: {fragments}, recipes: {self.recipes}, entries: {self.entries}"
        )


# Shorthand forms for simplicity


def literal(n):
    return Effect().recipe(Literal(n)).output()


def fetch(strWord):
    return literal(strWord) | Effect().fetch().output()
