print("This is a simple perimeter, area, volume calculator of a square")
side = input("Enter the length of 1 side of that shape:\n")
side = float(side)
def perimeter(side):
    return 4*side

def area(side):
    return side*side


def volume(side):
    return side**3



print(f"The perimeter of the shape is: {perimeter(side)}")
print(f"The area of the shape is: {area(side)}")
print(f"The volume of that shape is: {volume(side)}")
print("That was all, Thanks for using this!")