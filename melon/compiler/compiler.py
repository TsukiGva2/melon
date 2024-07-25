from .errors import Melon_CompilerInvalidExpr
from .tokstream import TokStream
from .types.literal import litnum
from .types.word import word


class Compiler(TokStream):
    def __init__(self):
        TokStream.__init__(self)

    def compile(self, words):
        self.start_line(words)

        for w in self.stream:
            try:
                yield litnum(w)
                continue
            except ValueError:
                # Multiple effects ( literal -> fetch )
                yield from word(w)
                continue

            raise Melon_CompilerInvalidExpr(f"Invalid word: {w}")
