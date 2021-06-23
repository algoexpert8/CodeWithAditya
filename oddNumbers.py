# create a generator that generates odd number from a user defined starting range till a user defined end range
# for that we have to use the for loop
# intro
print('ODD NUMBER GENERATOR')
start = int(input('Enter Starting Point:\n'))
end = int(input('Enter Ending Point:\n'))
for num in range(start,end+1):
    if num%2==1:
        print(num,end='\n')