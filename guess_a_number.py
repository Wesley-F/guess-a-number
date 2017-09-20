import random

# config
low = 1
high = 10
limit = 4

# helper functions
def show_start_screen():
    print("   _____                                  _   _                 _                 ")     
    print("  / ____|                         /\     | \ | |               | |                ")
    print(" | |  __ _   _  ___  ___ ___     /  \    |  \| |_   _ _ __ ___ | |__   ___ _ __   ")
    print(" | | |_ | | | |/ _ \/ __/ __|   / /\ \   | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|  ")
    print(" | |__| | |_| |  __/\__ \__ \  / ____ \  | |\  | |_| | | | | | | |_) |  __/ |     ")
    print("  \_____|\__,_|\___||___/___/ /_/    \_\ |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     ")  

def show_credits():
    print("This awesome game was created by")
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
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print("You win!")
    else:
        print("You are such a loser! The number was " + str(rand) + ".")

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
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
