#input the numbers from the user
import random
num1 = input("Enter 1st Number Here:\t")

num2 = input("Enter 2nd Number Here:\t")

#coverting the input string into numbers so that the calculator fumctions properly

num1 = float(num1)

num2 = float(num2)

#asking the operation from the user

operation = input("Enter Your Operation From - (+,-,*,/)\t")

#creating variables for the operations

sum = num1 + num2

difference = num1 - num2

product = num1 * num2

quotient = num1/num2

#creating an if else statement to print only the output of desired operation

if '+' in operation:
    print(f"The Sum Is =\t {sum}")

elif '-' in operation:
    print(f"The Difference Is =\t {difference}")

elif '*' in operation:
    print(f"The Product Is =\t {product}")

elif '/' in operation:
    print(f"The Quotient Is =\t {quotient}")

else:
    print("Invalid Input! Make sure you've entered in the correct format!")
rand = random.randint(-10,10)
print(f"Program Finished with Exit Code {rand} , Enter {rand} to exit console")
randnum = input('')
randnum = int(randnum)
#end