from .errors import Melon_CompilerInvalidExpr
from .tokstream import TokStream
from .types.build import litnum, word


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
                yield word(w)
                continue

            raise Melon_CompilerInvalidExpr(f"Invalid word: {w}")
