"""
Guess a Number A.I
Wesley F
"""

import random
import math


# helper functions
def show_start_screen():
    print("   _____                               _   _                 _                            _____   ")
    print("  / ____|                             | \ | |               | |                   /\     |_   _|  ")
    print(" | |  __ _   _  ___  ___ ___    __ _  |  \| |_   _ _ __ ___ | |__   ___ _ __     /  \      | |    ")
    print(" | | |_ | | | |/ _ \/ __/ __|  / _` | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|   / /\ \     | |    ")
    print(" | |__| | |_| |  __/\__ \__ \ | (_| | | |\  | |_| | | | | | | |_) |  __/ |     / ____ \ _ _| |_ _ ")
    print("  \_____|\__,_|\___||___/___/  \__,_| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|    /_/    \_(_)_____(_)")
    print()

                                                                                                                                                                                                  
def show_credits():
    print("This awesome game was created by")                                                            
    print("     _ _ _         _                                                 ")
    print("    | | | |___ ___| |___ _ _                                         ")
    print("    | | | | -_|_ -| | -_| | |                                        ")
    print("    |_____|___|___|_|___|_  |                                        ")
    print("                        |___|                                        ")
    print("                                                                     ")
    print("     _____     _       _              ___       _    ___ ___ ___ ___ ")
    print("    |     |___| |_ ___| |_ ___ ___   |_  |___ _| |  |_  |   |_  |_  |")
    print("    |  |  |  _|  _| . | . | -_|  _|  |  _|   | . |  |  _| | |_| |_| |")
    print("    |_____|___|_| |___|___|___|_|    |___|_|_|___|  |___|___|_____|_|")
    print()

    
def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """
    return (current_low + current_high) // 2

def get_range():
    current_low = int(input("Pick the lowest number I could guess."))
    print()
    current_high = int(input("Pick the highest number I could guess."))
    print()
    
    return current_low, current_high


def pick_number(current_high, current_low, limit):
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    input("Think a number between " + str(current_low) + " and " + str(current_high) + " and then press enter. I will have " + str(limit) + " tries to guess your number.")
    print()
    
    
def check_guess(guess, tries, limit):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    while True:
        print("Guess number " + str(tries + 1) + " out of " + str(limit) + ": " + str(guess))
        print()
        check_number = input("Is this number too high, too low or is it your number? (high, low, correct)")
        print()
        
        if check_number.lower() == "correct" or check_number.lower() == "c":
            return 0
        elif check_number.lower() == "high" or check_number.lower() == "h":
            return 1
        elif check_number.lower() == "low" or check_number.lower() == "l":
            return -1
        else:
            print("I do not understand. Please try again.")
            print()
        
    
def show_result(tries, check, limit):
    """
    Says the result of the game. (The computer might always win.)
    """
    if check != 0 and tries == limit:
        print("I think you made a mistake somewhere.")
    else:    
        print("I got your number in " + str(tries) + " tries!")
    print()
    

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        print()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
            print()
            

def play():
    check = -1
    tries = 0

    current_low, current_high = get_range()
    
    limit = math.ceil(math.log(current_high - current_low + 2 , 2))

    pick_number(current_high, current_low, limit)
    
    while check != 0 and tries < limit:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess, tries, limit)

        if check == -1:
            # adjust current_low
            current_low = guess + 1
        elif check == 1:
            # adjust current_high
            current_high = guess - 1
        tries += 1
        
    show_result(tries, check, limit)



# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



