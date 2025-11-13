def WelcomeMessage():

    WelcomeMessageString = '''Welcome to NRiP-V1
    
    This tool is an implementation of the Newton Raphson Method for Finding roots VIA Iteration formulae

    There are some exceptions as per the Newton Raphson:
    - It will diverge if you try a point where f(x) has a shallow gradient
    - The point musn't go to a stationary point
    - NO complex roots please

    To see/turn Off Logs, go to config.py and set ENV to 'DEV'

    Runtime: python 3.13.2

    NOTE: ONLY FOR POLYNOMIALS, NOT OTHER TYPES OF FUNCTIONS AS I HAVEN'T MADE THE DERRIVATIVE CALCULATOR READY FOR THAT

    Write polynomials in this form:

        1X^3 - 3X + 5
        coefficientX^exponent

    And with That, A теперь наслаждайтесь!
'''
    print('-' * 6)
    print(WelcomeMessageString)
    print('-' * 6)

    return