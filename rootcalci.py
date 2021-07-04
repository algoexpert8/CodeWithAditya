import numpy
operation = input("Enter SQRT for square root , or CBRT for cube root:\t")
number = float(input('Enter the number:\n'))
if operation=='SQRT':
    print(numpy.sqrt(number))
elif operation=='CBRT':
    print(numpy.cbrt(number))
else:
    print("Error! invalid input please try again!")