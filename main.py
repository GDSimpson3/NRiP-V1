

from modules.core.MainRecursion.MainRecursion import MainRecursion
from modules.system.Startup.WelcomeMessage import WelcomeMessage
from modules.system.inputProcessor.inputProcessor import InputProcessorMain


WelcomeMessage()

FxInputed = InputProcessorMain("Please Enter the Polynomial: ")

DpAccuracy = int(input("To how many Decimal places do you want the root?: "))

StartingPoint = int(input("Please enter a Starting point: "))

# print(FxInputed)

print(MainRecursion(FxInputed,StartingPoint,DpAccuracy))