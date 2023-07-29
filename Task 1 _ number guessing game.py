# A SIMPLE RANDOM GUESSING GAME
import random
name=input('Hey, Welcome to the game!\nPlease enter your name to get started:')
print('RULES & REGULATIONS\n*You will be given a total of 10 attempts to guess the number.\n*Everytime you enter an number, you will be noified if the number is lower or higher or equal to the random number.\n*If you guess the number correctly you win..\n*Else, you lose')
while True:
    print('All the best',name)
    random_number=random.randint(1,100)
    for i in range(10):
        user=int(input('Enter a number of your choice in the range of 1 to 100'))
        if user>random_number:
            print('That\'s too high,Try again')
        elif user<random_number:
            print('That\'s too low,Try again')
        else:
            print('Hurray, you found the answer.\nCongrats, you won !!!')
            break
    print('Hm, the random number was',random_number)
    play_again=input('Would you like to play again?\nY/N:')
    if (play_again=='Y' or play_again=='y'):
        continue
    else:
        print('Hope you enjoyed the game')
        break
    
    
