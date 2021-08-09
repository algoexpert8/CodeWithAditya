base = input("Enter the base value (the number):\n")
power = input("Enter the power value (the exponent):\n")
base, power = int(base),int(power)
def answer(base,power):
    return base**power
print(f"{base} raised to the power {power} is {answer(base,power)}")
