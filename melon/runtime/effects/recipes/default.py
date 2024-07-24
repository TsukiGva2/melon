from .constant import Constant


def Literal(n):
    return Constant(lambda: n)
