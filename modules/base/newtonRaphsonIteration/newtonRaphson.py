from modules.functional.computeFX.FX import FX
from modules.functional.differentiate.differentiate import Differentiate


def NewtonRaphsonIteration(Polynomial: list[list[str]], xn:int):
    DerivativeFx = Differentiate(Polynomial)

    FXn = FX(Polynomial,xn)
    DydxXn = FX(DerivativeFx, xn)

    XnPlus1 = xn - (FXn / DydxXn)


    return XnPlus1