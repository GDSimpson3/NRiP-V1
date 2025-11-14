from modules.base.newtonRaphsonIteration.newtonRaphson import NewtonRaphsonIteration
from modules.utils.logger.logger import LOG


def MainRecursion(Polynomial:list[list[str]], xn:int, DPAcuraccy:int) -> int:

    RootIterations: list[int] = [xn]

    # RootIterations.append()

    # XnP1 = NewtonRaphsonIteration(Polynomial, RootIterations[-1])

    while True:

        XnP1 = NewtonRaphsonIteration(Polynomial, RootIterations[-1])

        LOG(f'ROOT ITERATRIONS {RootIterations}')


        LOG(f'CHECK {round(RootIterations[-1],DPAcuraccy) == round(XnP1,DPAcuraccy)}')

        if round(RootIterations[-1],DPAcuraccy) == round(XnP1,DPAcuraccy):
            return XnP1
        
        RootIterations.append(XnP1)


    # while not (round(RootIterations[-1],DPAcuraccy) == round(XnP1,DPAcuraccy)):
    #     LOG(f'ROOT ITERATIONS ARRAY {RootIterations}')
    #     RootIterations.append(XnP1)
    #     XnP1 = NewtonRaphsonIteration(Polynomial, XnP1)

    # return XnP1
