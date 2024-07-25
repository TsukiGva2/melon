from .errors import Melon_CompilerUnexpectedEOF


class TokStream:
    def __init__(self):
        self.stream = None

    def start_line(self, line):
        self.stream = iter(line.split())

    # utils
    def next(self, caller):
        try:
            return next(self.stream)
        except StopIteration:
            raise Melon_CompilerUnexpectedEOF(
                f"Unexpected EOF in definition for '{caller}'."
            )  # TODO
