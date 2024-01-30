# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


def game_level():
    name = input('Enter your name here: ')
    print(f'Hello {name}, which level would you like to play?\n') 
    level = input("Type either \'easy\',\'medium\', or \'hard\': ")

    if level == 'easy':
        print('You have chosen easy')
        return easy
    elif level == 'medium':
        print('You have chosen medium')
        return medium
    elif level == 'hard':
        print('You have chosen hard')
        return hard
    else:
        print('You have entered an incorrect option')


random_number = random.randint(1,100)
guess = 0

game_level()
print(random_number)

