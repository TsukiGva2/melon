from typing import Any

from melon.runtime.effects.effects import Effect
from melon.runtime.effects.recipes.viewer import Viewer


def show_it(word: Any) -> None:
    print(word)


Show: Viewer = Viewer(show_it)
show: Effect = Show
