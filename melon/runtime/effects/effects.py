# TODO: stack transformation checking

from collections import deque
from enum import Enum
from typing import Tuple, Union

from .context import EffectContext

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

    def __or__(self, effect):
        if not isinstance(effect, Effect):
            raise TypeError("Can't join effect with non-effect")

        # append(effects.fragments)
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
        Get entry from context (stack)
        """
        self.fragments.append(Fragment.IN)

        return self

    def fetch(self):
        """
        Fetch an Effect from an entry to the entry list
        """
        self.fragments.append(Fragment.FETCH)

        return self

    def recipe(self, r: Recipe):
        self.recipes.append(r)
        self.fragments.append(Fragment.APPLY)

        return self

    # Access controllers

    def take_entry(self, entries, context, reason="input"):
        # print(f"\t• {reason.upper()}")
        entry = next(entries)
        return entry

    def take_recipe(self, recipes, reason="apply"):
        recipe = next(recipes)
        # print(f"\t• {reason.upper()} {type(recipe).__name__.upper()}")
        return recipe

    # Appliers

    def apply_recipe(self, target, recipes):
        return self.take_recipe(recipes)(target)

    # Resolver

    def resolve_effects(self, context, entries):
        entry = self.take_entry(entries, context, reason="fetch")
        effect = context.resolve(entry)

        with EffectContext(
            entries, context.scope, mode=context.mode, name=f"{entry}"
        ) as ctx:
            # handle accessing inputs in case entries is too small
            ctx.set_underflow_handler(context)
            return ctx.apply(effect)

    # effect application

    def apply(self, context):
        entries = context.ask(self.fragments.count(Fragment.IN))
        recipes = iter(self.recipes)

        for fragment in self.fragments:
            match fragment:
                case Fragment.FETCH:
                    entries = self.resolve_effects(context, entries)
                case Fragment.APPLY:
                    entries = self.apply_recipe(entries, recipes)
                case Fragment.END:
                    break  # TODO: signal end or do something

        context.output(entries)


# Effect >> Recipe
# Effect | Effect

# Shorthand forms for simplicity


def literal(n: Union[str, int]) -> Effect:
    return Effect() >> Literal(n)


def fetch_word(strWord: str) -> Tuple[Effect, Effect]:
    return (literal(strWord), Effect().input().fetch())
