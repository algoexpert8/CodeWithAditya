# this will convert from celsius fahrenheit or vice-versa depending on the choice..
# c to f = (C × 0.55555555555) +32
# f to c = (F -32) * 0.55555555555
# ask the user to input whether they want to convert from c to f or f to c
function = input('Enter C to convert from C to F or enter F to convert from F to C\n')
number = input('Enter the temperature value (just enter the numbers):\n')
number = float(number)
fc = (number-32)*0.55555555555
cf = number*9/5 + 32
if function == 'C':
    print(f'{number} celsius into fahrenheit is = {cf} fahrenheit')
elif function =='F':
    print(f'{number} fahrenheit into celsius is = {fc} celsius')
else:
    print('ERROR ! INVALID INPUT PLEASE TRY AGAIN')