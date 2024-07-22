from .tokenizer import Tokenizer


class Compiler(Tokenizer):
    def __init__(self):
        Tokenizer.__init__(self)

    def compile(self, words):
        self.words = iter(words.split())

        for w in self.words:
            try:
                yield self.literal(self.number(w))
                continue
            except ValueError:
                yield self.word(self.is_word(w))
                continue
