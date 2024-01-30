# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


def game_level():
    """
    Game start function to request user's name and difficulty they wish to play
    """
    name = input('Enter your name here: ')
    print(f'Hello {name}, which level would you like to play?\n') 
    level = input("Type either \'easy\',\'medium\', or \'hard\': ")

    if level == 'easy':
        print('You have chosen easy')
        
    elif level == 'medium':
        print('You have chosen medium')
        
    elif level == 'hard':
        print('You have chosen hard')
        
    else:
        print('You have entered an incorrect option')

    return level


def Generate_random_value(chosen_level):
    """
    Generates value based on game level chosen.
    """
    if chosen_level == 'easy':
        random_number = random.randint(1,20)
        print(random_number)
    elif chosen_level == 'medium':
        random_number = random.randint(1,50)
        print(random_number)
    elif chosen_level == 'hard':
        random_number = random.randint(1,100)
        print(random_number)
    else:
        print('other')

chosen_level = game_level()
Generate_random_value(chosen_level)

guess = 0



