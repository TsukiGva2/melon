import re

from .errors import Melon_CompilerError, Melon_CompilerUnexpectedEOF


class Tokenizer:
    def __init__(self):
        self.words = iter([])

        # NOTE: very permissive
        self.match_word = re.compile(
            r"[?/A-Za-z!@#$%&*()\[\]^~'`\"\\+=-_.,><{}:;][?/A-Za-z0-9!@#$%&*()\[\]^~'`\"\\+=-_.,><{}:;]*"
        )

    # utils
    def next(self, caller):
        try:
            return next(self.words)
        except StopIteration:
            raise Melon_CompilerUnexpectedEOF(
                f"Unexpected EOF in definition for '{caller}'."
            )  # TODO

    def is_word(self, w):
        if self.match_word.match(w):
            return w

        raise Melon_CompilerError(f"Invalid identifier '{w}'")

    def number(self, num):
        n = float(num)  # TODO @DESIGN @OPTIMIZATION: separate int/float types
        return n
