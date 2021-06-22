#pehle user se poocho ki usko cube root karna hai ya square root
#phir user se number mango
import numpy
import math
import random
from numpy.random import rand, random_integers
func = input('Enter SQRT for square root and CBRT for cube root:\t')
number = input('OK, now enter the number:\t')
number = float(number)
#if else se answer do
if func=='cbrt' or func=='CBRT':
    cuberoot = numpy.cbrt(number)
    print(f"The cube root of {number} is = {cuberoot}")

elif func=='sqrt' or func=='SQRT':
    squareroot = numpy.sqrt(number)
    print(f'The square root of {number} is = {squareroot}')

elif number<0:
    print(f"{func} OF A NEGATIVE NUMBER IS NOT DEFINED")

randomnumber = random.randint(-10,10)
input(f"Program Finished With Exit Code {randomnumber} , Press Enter To Exit Console")