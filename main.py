

from modules.system.Startup.WelcomeMessage import WelcomeMessage
from modules.system.inputProcessor.inputProcessor import InputProcessorMain


WelcomeMessage()

FxInputed = InputProcessorMain("Please Enter the Polynomial: ")

DpAccuracy = int(input("To how many Decimal places do you want the root?: "))

print(FxInputed)