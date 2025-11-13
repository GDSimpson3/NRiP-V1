from config import ENVIRONMENT
from modules.system.inputProcessor.inputFormatter import InputFormatter


def InputProcessorMain(Message) -> list[list[str]]:
    RawStrInput = str(input(Message))

    if ENVIRONMENT == 'DEV':
        RawStrInput = '1X^3 - 3X + 5'
        # RawStrInput = '8x^3 -40x^2 + 46x -15'

    
    return InputFormatter(RawStrInput)

 