start = input('Enter Starting range:\n')
end = input('Enter Ending Range:\n')
start = int(start)
end = int(end)
for i in range(start,end+1):
    if i%2==0:
        print(i)