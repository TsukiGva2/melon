import re

from melon.compiler.errors import Melon_CompilerError
from melon.runtime.effects.effects import Effect, fetch_word

# NOTE: very permissive
word_expr: re.Pattern = re.compile(
    r"[?/A-Za-z!@#$%&*()\[\]^~'`\"\\+=-_.,><{}:;][?/A-Za-z0-9!@#$%&*()\[\]^~'`\"\\+=-_.,><{}:;]*"
)


def must_match(word: str, expr: re.Pattern) -> str:
    if expr.match(word):
        return word

    raise Melon_CompilerError(f"Invalid identifier '{word}'")


def word(word: str) -> Effect:
    literal, fetch_eff = fetch_word(must_match(word, word_expr))

    yield literal
    yield fetch_eff
