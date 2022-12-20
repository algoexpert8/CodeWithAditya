import random
print("ROCK! PAPER! SCISSOR!")
instructions= '''THIS GAME HAS ONLY 1 POINT, SO THE ONE WHO WINS FIRST, IS THE WINNER. THIS 
IS A ROCK PAPER SCISSOR GAME IN WHICH YOU HAVE TO ENTER YOUR CHOICE AND THE CPU WILL GIVE ITS 
CHOICE. PRESS ENTER TO PROCEED.'''
print(instructions)
proceed = input('Press enter to proceed:\t')
choic = ('S','R','P')
player = input('Enter R for rock, P for Paper or S for scissor:\n')
print('Your choice: ', player)
cpu = random.choice(choic)
print('CPU: ', cpu)
if player == 'R' and cpu == 'S':
    print('Yay! you won')
elif player == 'R' and cpu == 'P':
    print('Oh no! You lost')
elif player == 'R' and cpu == 'R':
    print('It is a draw! Play again')
elif player == 'S' and cpu == 'R':
    print('Oh no! You lost')
elif player == 'S' and cpu == 'S':
    print('It is a draw! Play again')
elif player == 'S' and cpu == 'P':
    print('Yay! you won')
elif player == 'P' and cpu =='P':
    print("It is a draw! Play again")
elif player == 'P' and cpu == 'S':
    print('Oh no! you lost')
elif player =='P' and cpu == 'R':
    print('Yay! you won')
else:
    print('Error! Invalid input! Please try again')
