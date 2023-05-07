import random, os, platform


magic_number = 5
min = 1
max = 10
max_tries = 3

# Clear terminal
os.system("cls" if platform.system() == "Windows" else "clear")

# Print game intro
print("-"*50, "MAGIC NUMBER", "-"*50)
print(f"I have a number between {min} and {max}. Can you guess it?")
print(f"You can try {max_tries} times.")

# while True:
