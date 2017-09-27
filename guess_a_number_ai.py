import random

# config
low = 1
high = 1000


# helper functions
def show_start_screen():
    print("   _____                               _   _                 _                            _____   ")
    print("  / ____|                             | \ | |               | |                   /\     |_   _|  ")
    print(" | |  __ _   _  ___  ___ ___    __ _  |  \| |_   _ _ __ ___ | |__   ___ _ __     /  \      | |    ")
    print(" | | |_ | | | |/ _ \/ __/ __|  / _` | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|   / /\ \     | |    ")
    print(" | |__| | |_| |  __/\__ \__ \ | (_| | | |\  | |_| | | | | | | |_) |  __/ |     / ____ \ _ _| |_ _ ")
    print("  \_____|\__,_|\___||___/___/  \__,_| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|    /_/    \_(_)_____(_)")
                                                                                                                                                                                                  
def show_credits():
    print("This awesome game was created by")
    print()
    print()
    print("$$\      $$\                     $$\                           $$$$$$$$\                            $$\                                $$\                         ") 
    print("$$ | $\  $$ |                    $$ |                          $$  _____|                           $$ |                               $$ |                        ") 
    print("$$ |$$$\ $$ | $$$$$$\   $$$$$$$\ $$ | $$$$$$\  $$\   $$\       $$ |    $$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$$\  $$\  $$\  $$\  $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  ") 
    print("$$ $$ $$\$$ |$$  __$$\ $$  _____|$$ |$$  __$$\ $$ |  $$ |      $$$$$\ $$  __$$\ $$  __$$\ $$  _____|$$  __$$\ $$ | $$ | $$ | \____$$\\_$$  _|  $$  __$$\ $$  __$$\ ")
    print("$$$$  _$$$$ |$$$$$$$$ |\$$$$$$\  $$ |$$$$$$$$ |$$ |  $$ |      $$  __|$$ |  \__|$$$$$$$$ |\$$$$$$\  $$ |  $$ |$$ | $$ | $$ | $$$$$$$ | $$ |    $$$$$$$$ |$$ |  \__|")
    print("$$$  / \$$$ |$$   ____| \____$$\ $$ |$$   ____|$$ |  $$ |      $$ |   $$ |      $$   ____| \____$$\ $$ |  $$ |$$ | $$ | $$ |$$  __$$ | $$ |$$\ $$   ____|$$ |      ") 
    print("$$  /   \$$ |\$$$$$$$\ $$$$$$$  |$$ |\$$$$$$$\ \$$$$$$$ |      $$ |   $$ |      \$$$$$$$\ $$$$$$$  |$$ |  $$ |\$$$$$\$$$$  |\$$$$$$$ | \$$$$  |\$$$$$$$\ $$ |      ") 
    print("\__/     \__| \_______|\_______/ \__| \_______| \____$$ |      \__|   \__|       \_______|\_______/ \__|  \__| \_____\____/  \_______|  \____/  \_______|\__|      ") 
    print("                                               $$\   $$ |                                                                                                          ") 
    print("                                               \$$$$$$  |                                                                                                          ") 
    print("                                                \______/                                                                                                           ") 
    
def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """
    return (current_low + current_high) // 2

def pick_number():
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    input("Think a number between " + str(low) + " and " + str(high) + " and then press enter.")
                   
def check_guess(guess):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    print (str(guess))
    check_number = input("Is this number too high, too low or is it your number? (High, Low, Correct)")
    if check_number == "Correct":
        return 0
    elif check_number == "High":
        return 1
    elif check_number == "Low":
        return -1
        
    
def show_result():
    """
    Says the result of the game. (The computer might always win.)
    """
    print("I got your number!")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            # adjust current_low
            current_low = guess + 1
        elif check == 1:
            # adjust current_high
            current_high = guess - 1

    show_result()


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



