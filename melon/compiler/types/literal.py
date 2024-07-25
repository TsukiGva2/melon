from melon.runtime.effects.effects import Effect, literal


def number(num: str) -> float:
    n = float(num)  # TODO @DESIGN @OPTIMIZATION: separate int/float types
    return n


def litnum(num: str) -> Effect:
    return literal(number(num))
