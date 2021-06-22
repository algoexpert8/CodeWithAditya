import math

#pehle user se pucho ki usko hcf calculate karna hai ya phir lcm
operation = input('Choose an operation from HCF or LCM:\t')

#abhi user se numbers le lo, aur phir wo numbers ko integers me convert karlo
num1 = input('Enter First Number:\t')
num1 = int(num1)
num2 = input('Enter Second Number:\t')
num2 = int(num2)
#abhi hcf aur lcm ke variables bana lo
hcf = math.gcd(num1,num2)
lcm = math.lcm(num1,num2)
#abhi if-else-elif statement banao taki user ko hcf/lcm hi mile
if operation=='hcf' or operation=='HCF':
    print(f"The HCF (Highest Common Factor Of {num1} and {num2} is = {hcf}")
elif operation=='lcm' or operation=='LCM':
    print(f'The LCM (Least Common Multiple) of {num1} and {num2} is = {lcm}')
else:
    print('Error : Invalid Input')

input('Program Finished , Press enter to exit console')
#end