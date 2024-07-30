# TODO: stack transformation checking

from collections import deque
from enum import Enum
from typing import Tuple, Union

from melon.runtime.modes import RuntimeMode

from .context import EffectContext

# from melon.helpers.function import apply
from .recipes.default import Literal
from .recipes.recipe import Recipe

# from .errors import InvalidFragment

Fragment = Enum("Fragment", ["FETCH", "IN", "APPLY", "BUILD", "CLOSE", "END"])


# definitions


class Effect:
    def __init__(self):
        self.fragments = deque([])
        self.recipes = deque([])  # Reducers, Mappers and Filters

        self.bound_ctx = None

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

    def bind(self, ctx):
        self.bound_ctx = ctx

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

    def build(self):
        self.fragments.append(Fragment.BUILD)
        return self

    def build_close(self):
        self.fragments.append(Fragment.CLOSE)
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

        eff = effect.bound_ctx
        if eff is None:
            eff = EffectContext(context.scope, mode=context.mode, name=f"{entry}")

        with eff as ctx:
            ctx.set_inputs(entries, fallback=context.inputs)
            return ctx.apply(effect)

    # effect application

    def eval_fragments(self, context, entries, recipes):
        for fragment in self.fragments:
            match fragment:
                case Fragment.FETCH:
                    entries = self.resolve_effects(context, entries)
                case Fragment.APPLY:
                    entries = self.apply_recipe(entries, recipes)
                case Fragment.END:
                    break  # TODO: signal end or do something

        context.output(entries)

    def compile_fragments(self, context):
        context.output(self)

    def apply(self, context):
        # BUILD -> eval only setmodes
        # CLOSE -> go back to immediate

        # (     <- setmode BUILD (Word + fetch)
        #   Word  <- Word (Word + fetch)
        #   Word2 <- Word (Word + fetch)
        #   1     <- Literal
        #   'a    <- Literal
        # )     <- setmode CLOSE (Word + fetch)
        # Melon <- Assignment (Word + fetch)

        if context.mode == RuntimeMode.IMMEDIATE:
            entries = context.ask(self.fragments.count(Fragment.IN))
            recipes = iter(self.recipes)

            self.eval_fragments(context, entries, recipes)
        else:
            self.compile_fragments(context)


# Effect >> Recipe
# Effect | Effect

# Shorthand forms for simplicity


def literal(n: Union[str, int]) -> Effect:
    return Effect() >> Literal(n)


def fetch_word(strWord: str) -> Tuple[Effect, Effect]:
    return (literal(strWord), Effect().input().fetch())
