import random, os, platform

min = 1
max = 10

# Clear terminal
os.system("cls" if platform.system() == "Windows" else "clear")

# Print game intro
print("-"*50, "MAGIC NUMBER", "-"*50)
print(f"I have a number between {min} and {max}. Can you guess it?")

while True:
    magic_number = 5
    max_tries = 3
    print(f"You can try {max_tries} times.")

    player_guess = input("Your guess?")

    while player_guess != magic_number:
        os.system("cls" if platform.system() == "Windows" else "clear")
        max_tries -= 1

        if max_tries == 0:
            break

        print(f"Wrong guess. You have {max_tries}. Try Again.")
        player_guess = input("Your guess?")
    
    # check results
    os.system("cls" if platform.system() == "Windows" else "clear")
    if player_guess == magic_number:
        print(f"You wind! {magic_number} was my number :)))")
    else:
        print(f"My number was {magic_number}.")
        print("Game over :(((")

    # ask for a new game
    player_choice = input("Do you want to play again? (y/n)")
    if player_choice == "n":
        exit()