from typing import final

from shell import Shell


@final
class Command:
    def __init__(self, command: str = ""):
        self.command: str = command

        self.shell = Shell()

    def execute(self) -> int:
        code = self.shell.run(self.command).code

        return code
