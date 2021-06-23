# create a generator that generates even numbers from a user defined starting point till a user defined end point
# we have to use the for loop for this
# intro
print('EVEN NUMBER GENERATOR')
# taking the range from the user
start = int(input('Enter Starting Point:\n'))
end = int(input('Enter Ending Point:\n'))
for num in range(start,end+1):
    if num%2==0:
        print(num,end='\n')