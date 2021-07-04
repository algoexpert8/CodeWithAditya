print('BASIC CALCULATOR')
num1 = input('Enter first number here:\n')
num2 = input('Enter second number here:\n')
num1 = float(num1)
num2 = float(num2)
operation = input('Enter an operation from +,-,* or /\n')
if '+' in operation:
    print('The sum is=',num1+num2)
elif '-' in operation:
    print('The difference is=',num1-num2)
elif '*' in operation:
    print('The product is=',num1*num2)
elif '/' in operation:
    print('The quotient is=',num1/num2)
else:
    print('ERROR! INVALID INPUT, PLEASE TRY AGAIN')