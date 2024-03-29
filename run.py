# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import colorama
from colorama import Fore, Back, Style, init
init(autoreset=True)


def user_name():
    """
    Game start function to request user's name and difficulty they wish to
    play.  Name input has a while loop with strip() method to ensure anything
    other than whitespace is valid.
    """
    while True:
        try:
            name = input('Enter your name here: ')
            if not name.strip():
                raise ValueError(Fore.RED + 'Not a valid name')
            elif not name.isalpha():
                raise ValueError(Fore.RED + 'Invalid name. Please enter '
                                 'alphabetic characters only.')
            break
        except ValueError as e:
            print(e)

    return name


def choose_level(name):
    """
    level selection has a while loop to ensure a level is chosen otherwise
    error will be given and user would again be prompted to enter a level.
    """

    print(f'\nHello {name}, The rules are simple:\n Guess which number I\'m'
          ' thinking of.\n If you are down to your last 3 attempts, you will '
          'receive some clues\n to help you.')

    while True:
        level = input("which level would you like to play?  Type either 'easy'"
                      ", 'medium', or 'hard': \n")

        if level.lower() in ['easy', 'medium', 'hard']:
            print(f'\nGreat {name}, you have chosen {level}\n')
            break
        else:
            print(Fore.RED + f'Sorry {name}, you have entered an invalid '
                  'option. Please choose a valid game difficulty\n')

    return level


def generate_random_value(name, chosen_level):
    """
    Generates value based on game level chosen.
    """
    random_number = 0
    attempts = 0

    if chosen_level.lower() == 'easy':
        random_number = random.randint(1, 20)
        attempts = 5
        print(f"I\'m thinking of a number, {name}! You have 5 attempts to\n "
              "guess which number it is.")
    elif chosen_level.lower() == 'medium':
        random_number = random.randint(1, 50)
        attempts = 8
        print(f"I\'m thinking of a number, {name}! You have 8 attempts to\n "
              "guess which number it is.")
    elif chosen_level.lower() == 'hard':
        random_number = random.randint(1, 100)
        attempts = 13
        print(f"I\'m thinking of a number, {name}! You have 13 attempts to\n "
              "guess which number it is.")
    else:
        print(Fore.RED + 'Invalid game level')

    return random_number, attempts


def approximity(guess, random_number, guessed_numbers, difference_list):
    """
    Returns the difference between the guess and the random number.
    """

    difference = abs(int(guess) - random_number)
    difference_list.append(difference)

    if 1 <= difference < 9:
        print(Fore.YELLOW + Style.BRIGHT + 'You\'re so close now!')

    if len(difference_list) >= 2:
        last_difference = difference_list[-1]
        penultimate_difference = difference_list[-2]

        if difference == 0:
            print(Fore.GREEN + Style.BRIGHT + 'Spot on!')
        elif last_difference < penultimate_difference:
            print('You\'re getting', Fore.RED + Style.BRIGHT + 'warmer!')
        elif last_difference > penultimate_difference:
            print('Oops! You\'re getting', Fore.BLUE + 'colder!')


def check_answer(name, random_number_and_attempts, chosen_level,
                 difference_list):
    """
    Checks if user's guess is correct, prevents repeating the same guess, and
    ensures the guess is within the valid range.
    """
    random_number, attempts = random_number_and_attempts
    guessed_numbers = []

    while attempts > 0:
        guess = input(f'Your guess (between 1 and '
                      f'{get_max_value(chosen_level)}): ')

        if guess.isdigit():
            guess = int(guess)
        else:
            print(Fore.RED + 'Invalid input. Please enter a number.')
            continue

        difference = approximity(guess, random_number, guessed_numbers,
                                 difference_list)

        if guess in guessed_numbers:
            print(Fore.RED + 'You already guessed that number. Try a '
                  'different one.')
            continue

        if 1 <= guess <= get_max_value(chosen_level):
            guessed_numbers.append(guess)

            if guess != random_number:
                print('Try again\n')
                attempts -= 1

                if attempts == 3:
                    print(Fore.BLUE + 'You have 3 attempts left, so here are '
                          'some clues to help!')
                    if random_number % 3 == 0 and random_number % 4 == 0:
                        print(Fore.BLUE + 'This number is divisible by 3 and'
                              ' 4\n')
                    elif random_number % 3 == 0 and random_number % 4 != 0:
                        print(Fore.BLUE + 'This number is divisible by 3 but '
                              'not divisible by 4\n')
                    elif random_number % 3 != 0 and random_number % 4 == 0:
                        print(Fore.BLUE + 'This number is divisible by 4 but '
                              'not divisible by 3\n')
                    elif random_number % 3 != 0 and random_number % 4 != 0:
                        print(Fore.BLUE + 'This number is not divisible by '
                              'neither 3 nor 4\n')
                elif attempts == 0:
                    print(Fore.RED + f'Sorry {name}, you have run out of '
                          f'attempts. Game over.  The correct answer was '
                          f'actually {random_number}')
                    break
            else:
                print(Fore.GREEN + f'Hooray, {name}! You guessed the correct '
                      'number!')
                break
        else:
            print(Fore.RED + f'Invalid guess. Please enter a number between 1 '
                  f'and {get_max_value(chosen_level)}.')

    return random_number, attempts


def get_max_value(chosen_level):
    """
    Returns the maximum valid value for the chosen difficulty level.
    """
    if chosen_level.lower() == 'easy':
        return 20
    elif chosen_level.lower() == 'medium':
        return 50
    elif chosen_level.lower() == 'hard':
        return 100
    else:
        return 1


guess = 0
difference_list = []


def main():
    """
    Run all program functions
    """
    chosen_name = user_name()

    while True:
        difference_list = []
        chosen_level = choose_level(chosen_name)
        random_number_and_attempts = generate_random_value(chosen_name,
                                                           chosen_level)
        check_answer(chosen_name, random_number_and_attempts, chosen_level,
                     difference_list)

        while True:
            play_again = input(Style.BRIGHT + 'Do you want to play again? '
                               '(yes/no): ')
            if play_again.lower() == 'yes':
                print(Fore.YELLOW + "That\'s the spirit")
                break
            elif play_again.lower() == 'no':
                print(Fore.YELLOW + "Thanks for playing. Goodbye!")
                return
            else:
                print(Fore.RED + "please only write \'yes\' or \'no\'")


main()
