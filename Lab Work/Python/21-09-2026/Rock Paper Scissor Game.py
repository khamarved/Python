# Rock Paper Scissor Game
import random

while True:

    print("***** Play The Rock Paper Scissor Game *****")
    print("Choose: rock, paper, scissor")

    computer = random.choice(["rock", "paper", "scissor"])

    user = input("Enter your choice: ").lower()

    print("Computer chose:", computer)
    print("You chose:", user)

    if user not in ["rock", "paper", "scissor"]:
        print("Invalid Choice!!!")
        break

    if user == computer:
        print("Game Draw!!!")
        break

    elif user == "rock" and computer == "scissor":
        print("You Win!!!")

    elif user == "paper" and computer == "rock":
        print("You Win!!!")

    elif user == "scissor" and computer == "paper":
        print("You Win!!!")

    else:
        print("Computer Wins!!!")
        