<h1 align='center'>Newton Raphson in Python - NRiP-V1</h1>

## Overall Concept

1) Start at X0 that is conceptually not far from the root.
2) Draw it's Tangent and find it's X axis intersection point and call it X1
3) From X1, find it's tangent line and it's X axis intersection and call it X2
4) So on so fourth till it converges to the root


Newton-Raphson Iteration formula: `XnPlus1 = Xn - (f(Xn) / f'(Xn))`


<h1 align='center'>MODULES</h1>

# Base

## NewtonRaphsonIteration

I: `Polynomial: list[list[str]], xn:int, n=0`

O: `XnPlus1, IterationCount`

It applies the Newton-Raphson iteration formula to find the next iteration

Formula: `XnPlus1 = Xn - (f(Xn) / f'(Xn))`


# Functional

Smaller programs that would be used by the base modules


## Computing FX

I: `Polynomial: List[List[str]]`, `X: Int`

O: `FX: Int`

Loop through each term and sum the multiplication of the coefficient with X raised to the terms exponent

## Derivative Calculation

I: `Polynomial: List[List[str]]`

O: `Polynomial: List[List[str]]`

It simply conducts a Power rule differentiation with each term. Constants are eriadicated and non existent terms aren't considered



# System

System programs such as Input processing

## Input Processing

**Input format**: `7X^6 + 4X^2 - 8X^3 + 3x + 3`

**I**: `Polynomial: string`

**O** `Polynomial: List[List[str]]`

### Input cleansing

Make all the X's Capital and Eradicate all blank spaces VIA Regex

### Decoding: 

Split through the Operators `['+','-']` into an array
 
`7X^6 + 4X^2 - 8X^3 + 3x + 3` --> `["7X^6", "4X^2", "-8X^3", "3x", "3"]`

Take each term, and split it into coefficient and exponent to leave the computed form

`["7X^6", "4X^2", "-8X^3", "3x", "3"]` --> `[["7","6"], ["4","2"], ["-8","3"], ["3","1"], ["3","0"]]`

Note: Special cases for exponents of 1 and 0


# Utils

Utilities such as error handling and logging

## Logger [UTIL]

Custom Logging module, Clears all logs when environment is set to Prod (`ENVIRONMENT != 'DEV'`)

## Custom Error Handler [UTIL]

Custom Error handling module

## Custom Time Sleeper [UTIL]

Custom Time handling module, Dissables in Prod (`ENVIRONMENT != 'DEV'`)
