import numpy
operation = input('Enter HCF for computing hcf, or LCM for computing lcm:\t')
number1 = input('OK, now enter 1st number:\n')
number2 = input('OK, now enter 2nd number:\n')
number1,number2 = int(number1), int(number2)
if operation == 'HCF':
    print(numpy.gcd(number1,number2))
elif operation == 'LCM':
    print(numpy.lcm(number1,number2))
else:
    print('Error!')