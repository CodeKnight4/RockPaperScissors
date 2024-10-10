import random

mylist = ["rock", "paper", "scissors"]
wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}  # Storing the wins here reduces the need for a massive if elif else block
test = False
compSelection = random.choice(mylist)

while not test:  # In case the user enters something incorrect, the computer will always be correct
    userChoice = input("Enter your choice: ").lower()
    if userChoice == "rock" or userChoice == "paper" or userChoice == "scissors":
        test = True

if userChoice == compSelection:
    print(f"You both played {userChoice.title()}, it is a draw")
elif wins[userChoice] == compSelection:
    print(f"{userChoice.title()} beats {compSelection.title()}, you win!")
else:
    print(f"{compSelection.title()} beats {userChoice.title()}, you lose!")
