class Doc:
    def __init__(self, word):
        # get documentation from docs or docstring
        self.word = word

        # find docs somehow
        self.docs = ...  # TODO


def docs(word):
    return Doc(word).docs
