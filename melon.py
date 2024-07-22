import sys
from typing import Final

from melon.engine import Melon
from repl.repl import MelonREPL


def main():
    melon: Final[Melon] = Melon()
    shell: Final[MelonREPL] = MelonREPL(melon)

    while True:
        try:
            shell.loop()
        except EOFError:
            print("\nEOF")
            return True
        # except Exception as err:
        #    print(f"\n| Exception: {err}")


if __name__ == "__main__":
    if not main():
        sys.exit(1)
