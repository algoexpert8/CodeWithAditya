# this is a calculator in python which will tell whether an object will float or sink in water
#the denser a substance in water , it wll sink
#therefore if an object is denser than water it will sink in water 
#thus if water is denser than an object then the object will float in water
print('DENSITY CALCULATOR')
print('THIS CALCULATOR WILL TELL WHETHER AN OBJECT CAN FLOAT OR SINK IN WATER')
print('YOU JUST HAVE TO ENTER THE DENSITY OF YOUR ITEM IN METRE^CUBE, BE REST ASSURED')
proceed = input('PRESS ENTER TO PROCEED:\t')
dense_item = input('Enter the density of the item (IN METRE^CUBE):\n')
dense_item = float(dense_item)
dense_water = 997
if dense_item>dense_water:
    print('The Item Is Denser Than Water. Thus It Will Sink In Water')
elif dense_item<dense_water:
    print('Water Is Denser Than The Item. Thus It Will Float In Water')
elif dense_water==dense_item:
    print('You Have Entered The Density Of Water!')
else:
    print('ERROR! INCORRECT INPUT! PLEASE TRY AGAIN')
