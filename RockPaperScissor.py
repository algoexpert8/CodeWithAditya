#first ask the user to input her his choice
import random
print("ROCK ! PAPER ! SCISSOR!")
instructions = 'THIS GAME HAS 1 POINT , SO THE ONE WHO WINS FIRST , IS THE WINNER. THIS IS A ROCK PAPER SCISSOR GAME IN WHICH YOU HAVE TO ENTER YOUR CHOICE AND THE AI BOT WILL GIVE HIS/HER CHOICE. PRESS ENTER TO PROCEED. THANK YOU AND ENJOY'
print(instructions)
proceed = input('Press Enter To Proceed:\t')
choic = ('S','R','P')
player = input('Enter R for Rock, P for Paper or S for scissor:\n')
print('Your choice: ',player)
cpu = random.choice(choic)
print('CPU: ',cpu)
if player=='R' and cpu=='S':
    print('Yay! You won')
elif player=='R' and cpu=='P':
    print('Oh No! You Lost!')
elif player=='R' and cpu=='R':
    print('It is a draw! Play again!')
elif player =='S' and cpu=='R':
    print('Oh No! You Lost!')
elif player=='S' and cpu=='S':
    print('It is a draw! Play again!')
elif player=='S' and cpu=='P':
    print('Yay! You Won!')
elif player=='P' and cpu=='P':
    print('It is a draw! play again!')
elif player=='P' and cpu=='R':
    print('Yay! You Won!')
elif player =='P' and cpu=='S':
    print('Oh No! You Lost!')
else:
    print('Error! Invalid Input! Please Try Again!')
randomnum = random.randint(-10,10)
input(f'Program finsihed with exit code {randomnum}. Press Enter To exit console\t')
