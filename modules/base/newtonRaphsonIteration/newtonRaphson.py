from modules.functional.computeFX.FX import FX
from modules.functional.differentiate import differentiate


def NewtonRaphsonIteration(Polynomial: list[list[str]], xn, n=0):
    DerivativeFx = differentiate(Polynomial)

    FXn = FX(Polynomial,xn)
    DydxXn = FX(DerivativeFx, xn)

    XnPlus1 = xn - (FXn / DydxXn)

    IterationCount = n + 1

    return {XnPlus1, IterationCount}