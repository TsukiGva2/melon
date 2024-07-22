import readline
from typing import final

readline.parse_and_bind("tab: complete")
readline.set_completer_delims(" \t\n`~!@#$%^&*()-=+[{]}\\|;:'\",<>/?")


# TODO: autocompletion
@final
class ReadLine:
    def __init__(self, prompt="> ", non_empty=True):
        self.prompt = prompt
        self.non_empty = non_empty

        self.line = ""

    def read(self):
        while (line := input(self.prompt)) == "" and self.non_empty:
            ...
        self.line = line
