import re

from melon.compiler.errors import Melon_CompilerError

from .literal import Literal
from .word import Word

# NOTE: very permissive
word_expr: re.Pattern = re.compile(
    r"[?/A-Za-z!@#$%&*()\[\]^~'`\"\\+=-_.,><{}:;][?/A-Za-z0-9!@#$%&*()\[\]^~'`\"\\+=-_.,><{}:;]*"
)


def must_match(word: str, expr: re.Pattern) -> str:
    if expr.match(word):
        return word

    raise Melon_CompilerError(f"Invalid identifier '{word}'")


def number(num: str) -> float:
    n = float(num)  # TODO @DESIGN @OPTIMIZATION: separate int/float types
    return n


def litnum(num: str) -> Literal:
    return Literal(number(num))


def word(word: str) -> Word:
    return Word(must_match(word, word_expr))
