# TODO: stack transformation checking

from collections import deque
from enum import Enum
from itertools import chain
from typing import Tuple, Union

# from melon.helpers.function import apply
from .recipes.default import Literal
from .recipes.recipe import Recipe

# from .errors import InvalidFragment

Fragment = Enum("Fragment", ["FETCH", "IN", "APPLY", "END"])


# definitions


class Effect:
    def __init__(self):
        self.fragments = deque([])
        self.recipes = deque([])  # Reducers, Mappers and Filters

        self.docs = ""
        self.entrylog = deque([])

    def __or__(self, effect):
        if not isinstance(effect, Effect):
            raise TypeError("Can't join effect with non-effect")

        # appendleft(effects.fragments)
        self.fragments = effect.fragments + self.fragments
        self.recipes = effect.recipes + self.fragments

        return self

    def __rshift__(self, recipe: Recipe):
        if not isinstance(recipe, Recipe):
            raise TypeError("Can't apply non-recipe to Effect entries")

        return self.recipe(recipe)

    # TODO: generate docs when Saving/Applying function (to fetch all things)
    # TODO: create a sandbox function, which only executes the function in a
    # virtual stack, and shows result
    def mkdocs(self): ...

    def input(self):
        """
        Get entry from runtime (stack)
        """
        self.fragments.appendleft(Fragment.IN)

        return self

    def fetch(self):
        """
        Fetch an Effect from an entry to the entry list
        """
        self.fragments.appendleft(Fragment.FETCH)

        return self

    def recipe(self, r: Recipe):
        self.recipes.appendleft(r)
        self.fragments.appendleft(Fragment.APPLY)

        return self

    # logging

    # TODO: this kinda slows everything down lol
    def annotate(self, output):
        inputs = " ".join(["n"] * self.fragments.count(Fragment.IN))
        fetched = " ".join(map(str, self.entrylog))
        output = " ".join(map(str, output))

        print(f"\tIn: ({inputs} {fetched}) -> Out: ({output})\n")

    # Access controllers

    def take_entry(self, reason="input"):
        print(f"\t• {reason.upper()}")

        entry = next(self.entries)
        self.entrylog.append(entry)

        return entry

    def take_recipe(self, reason="apply"):
        recipe = self.recipes.pop()

        print(f"\t• {reason.upper()} {type(recipe).__name__.upper()}")

        return recipe

    # Appliers

    def apply_recipe(self, target):
        return self.take_recipe()(target)

    # Resolvers

    def resolve_recipes(self, new_recipes):
        return new_recipes + self.recipes

    def resolve_inputs(self, fragments, runtime):
        return chain(self.entries, runtime.ask(fragments.count(Fragment.IN)))

    def resolve_fragments(self, runtime):
        entry = self.take_entry(reason="fetch")
        effect = runtime.resolve(entry)

        # applies come automatically with the fragments
        self.recipes = self.resolve_recipes(effect.recipes)

        fragments = effect.fragments
        self.entries = self.resolve_inputs(fragments, runtime)

        return fragments

    # TODO @OPTIMIZATION: Use lru_cache
    def resolve_effects(self, fragments, runtime):
        match fragments:
            case []:
                yield Fragment.END

            case [Fragment.FETCH, *tail]:
                yield from (
                    self.resolve_effects(
                        self.resolve_fragments(runtime) + deque(tail), runtime
                    )
                )

            case [Fragment.IN, *tail]:
                yield from self.resolve_effects(tail, runtime)

            case [head, *tail]:
                yield from (chain([head], self.resolve_effects(tail, runtime)))

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
                    Runtime.ask (4) ->   pop + appendleft x4 -> reverseiter [ 'stack 'a 'im 'hey ]

                    entries <- reverseiter [ 'stack 'a 'im 'hey ]
        """

        # Fetches + Inputs
        self.entries = runtime.ask(self.fragments.count(Fragment.IN))

        fragments = self.resolve_effects(self.fragments, runtime)

        for fragment in fragments:
            match fragment:
                case Fragment.APPLY:
                    self.entries = self.apply_recipe(self.entries)
                case Fragment.END:
                    break  # TODO: signal end or do something

        output = list(self.entries)

        self.annotate(output)

        runtime.put(*output)

        return fragments


# Effect >> Recipe
# Effect | Effect

# Shorthand forms for simplicity


def literal(n: Union[str, int]) -> Effect:
    return Effect() >> Literal(n)


def fetch_word(strWord: str) -> Tuple[Effect, Effect]:
    return (literal(strWord), Effect().input().fetch())
