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
            elif not name.isalpha():
                raise ValueError('Invalid name. Please enter alphabetic characters only.')
            break
        except ValueError as e:
            print(e)
        
    print(f'\nHello {name}, The rules are simple: Guess which number I\'m thinking of.')

    while True:
        level = input("which level would you like to play?  Type either 'easy', 'medium', or 'hard': \n")
        
        if level.lower() in ['easy', 'medium', 'hard']:
            print(f'\nGreat {name}, you have chosen {level}\n')
            break
        else:
            print(f'Sorry {name}, you have entered an invalid option. Please choose a valid game difficulty\n')

    return name, level

def generate_random_value(name, chosen_level):
    """
    Generates value based on game level chosen.
    """
    if chosen_level == 'easy':
        random_number = random.randint(1, 20)
        attempts = 5
        print(f"I\'m thinking of a number, {name}! You have 5 attempts to guess which number it is.")
    elif chosen_level == 'medium':
        random_number = random.randint(1, 50)
        attempts = 8
        print(f"I\'m thinking of a number, {name}! You have 8 attempts to guess which number it is.")
    elif chosen_level == 'hard':
        random_number = random.randint(1, 100)
        attempts = 13
        print(f"I\'m thinking of a number, {name}! You have 13 attempts to guess which number it is.")
    else:
        print('Invalid game level')

    return random_number, attempts

def approximity(guess, random_number, guessed_numbers, difference_list):
    """
    Returns the difference between the guess and the random number.
    """
    
    difference = abs(int(guess) - random_number)
    difference_list.append(difference)

    if 1 <= difference < 10:
            print('You\'re so close now!')

    if len(difference_list) >= 2:
        last_difference = difference_list[-1]
        penultimate_difference = difference_list[-2]

        if difference == 0:
            print('Spot on!')
        elif last_difference < penultimate_difference:
            print('You\'re getting warmer!')
        elif last_difference > penultimate_difference:
            print('Colder!')
        

def check_answer(name, random_number_and_attempts, chosen_level, difference_list):
    """
    Checks if user's guess is correct, prevents repeating the same guess, and ensures 
    the guess is within the valid range.
    """
    random_number, attempts = random_number_and_attempts
    guessed_numbers = []

    while attempts > 0:
        guess = input(f'Your guess (between 1 and {get_max_value(chosen_level)}): ')

        if guess.isdigit():
            guess = int(guess)
        else:
            print('Invalid input. Please enter a number.')
            continue

        difference = approximity(guess, random_number, guessed_numbers, difference_list)

        if guess in guessed_numbers:
            print('You already guessed that number. Try a different one.')
            continue

        if 1 <= guess <= get_max_value(chosen_level):
            guessed_numbers.append(guess)

            if guess != random_number:
                print('Try again\n')
                attempts -= 1

                if attempts == 3:
                    print('You have 3 attempts left, so here are some clues to help!')
                    if random_number % 3 == 0 and random_number % 4 == 0:
                        print('This number is divisible by 3 and 4\n')
                    elif random_number % 3 == 0 and random_number % 4 != 0:
                        print('This number is divisible by 3 but not divisible by 4\n')
                    elif random_number % 3 != 0 and random_number % 4 == 0:
                        print('This number is divisible by 4 but not divisible by 3\n')
                    elif random_number % 3 != 0 and random_number % 4 != 0:
                        print('This number is not divisible by neither 3 nor 4\n')
                elif attempts == 0:
                    print(f'Sorry {name}, you have run out of attempts. Game over.  The correct answer was actually {random_number}')
                    break
            else:
                print(f'Hooray, {name}! You guessed the correct number!')
                break
        else:
            print(f'Invalid guess. Please enter a number between 1 and {get_max_value(chosen_level)}.')

    return guess, guessed_numbers

def get_max_value(chosen_level):
    """
    Returns the maximum valid value for the chosen difficulty level.
    """
    if chosen_level == 'easy':
        return 20
    elif chosen_level == 'medium':
        return 50
    elif chosen_level == 'hard':
        return 100
    else:
        return 1

guess = 0
difference_list = []

def main():
    """
    Run all program functions
    """
    while True:
        chosen_name, chosen_level = game_level()
        random_number_and_attempts = generate_random_value(chosen_name, chosen_level)
        check_answer(chosen_name, random_number_and_attempts, chosen_level,difference_list)

        play_again = input('Do you want to play again? (yes/no): ')
        if play_again.lower() != 'yes':
            print('Thanks for playing. Goodbye!')
            break
main()