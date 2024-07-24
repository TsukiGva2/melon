from melon.compiler.compiler import Compiler
from melon.runtime.runtime import Runtime


class Melon:
    def __init__(self):
        self.state = Runtime()

        self.compiler = Compiler()
        self.compile = self.compiler.compile

    def execute(self, instructions):
        return self.state.execute(instructions)
