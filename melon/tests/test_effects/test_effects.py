import melon.runtime.effects.effects as effects
from melon.runtime.runtime import Runtime


def test_application():
    runtime = Runtime()
    eff = effects.fetch()

    runtime.execute((eff,))
