import random

choice = ("rock", "paper", "scissors")

player = None
computer = random.choice(choice)

player = input("What's your choice? (rock, paper,scissors):")

print(f"Player:{player}")
print(f"Computer:{computer}")

if player == computer:
        print("It's a tie !")
elif player == "rock" and computer == "scissors":
        print("You win !")
elif player == "paper" and computer == "rock":
        print("You win !")
elif player == "scissors" and computer == "paper":
        print("You win !")
else:
        print("You lose !")


