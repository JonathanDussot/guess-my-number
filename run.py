# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


def game_level():
    """
    Game start function to request user's name and difficulty they wish to play.
    name input has a while loop with strip() method to ensure anything other than whitespace 
    is valid.
    level selection has a while loop to ensure a level is chosen otherwise error will be given and 
    user would again be prompted to enter a level.
    """
    while True:
        try:
            name = input('Enter your name here: ')
            if not name.strip():
                raise ValueError('Not a valid name')
            break
        except ValueError as e:
            print(e)
        
    print(f'Hello {name}, which level would you like to play?\n')

    while True:
        level = input("Type either 'easy', 'medium', or 'hard': ")
        
        if level in ['easy', 'medium', 'hard']:
            print(f'Hello {name}, you have chosen {level}')
            break
        else:
            print(f'Sorry {name}, you have entered an invalid option. Please choose a valid game difficulty')

    return level


def generate_random_value(chosen_level):
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
        print('Invalid game level')
       

chosen_level = game_level()
generate_random_value(chosen_level)

guess = 0



