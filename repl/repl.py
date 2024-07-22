from typing import final, override

from .input import ReadLine


class REPL:
    """
    Read
    Eval
    -Print-
    Loop
    """

    def __init__(self): ...

    def read(self): ...
    def eval(self): ...

    # def print(self): ...

    @final
    def loop(self):
        while True:
            self.read()
            self.eval()


@final
class MelonREPL(REPL):
    def __init__(self, engine):
        self.engine = engine

        self.prompt: ReadLine = ReadLine("melon> ")

    @override
    def read(self):
        self.prompt.read()

    @override
    def eval(self):
        command = self.engine.compile(self.prompt.line)

        self.engine.execute(command)
