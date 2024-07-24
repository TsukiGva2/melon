from melon.runtime.stack.effects import Effect


class Doc:
    def __init__(self, word):
        # get documentation from docs or docstring
        self.word = word

        # find docs somehow
        self.docs = ...  # TODO


getDoc = Effect().reduce(Doc)


class GetDoc(Effect):
    def __init__(self):
        Effect.__init__(self)
