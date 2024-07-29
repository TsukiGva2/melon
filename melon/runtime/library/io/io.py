from melon.runtime.effects.recipes.default import Constant
from melon.runtime.effects.recipes.viewer import Viewer

read: Constant = Constant(input)
show: Viewer = Viewer(print)
