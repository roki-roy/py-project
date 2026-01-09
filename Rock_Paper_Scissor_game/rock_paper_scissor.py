"""

Warking flow of project:-

1. Input from user's (Rock, Paper, Scissor)
2. Computer choise's Randomly not Conditionaly.
3. Resoult print

Choes:-
A- Rock

Rock - Rock = tie
Rock - Paper = Paper wine
Rock - scissor = Rock wine

B- Paper

Paper - Paper = tie
Paper - Rock = Paper wine
Paper - Scissor = Scissor wine

C- Scissor

Scissor - Scissor = tie
Scissor - Rock = Rock wine
Scissor - Paper = Scissor wine

"""

import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your choice = Rock, Paper, Scissor= ")
computer_choice = random.choice(item_list)

print(f"user choice {user_choice} computer choice {computer_choice}")

if user_choice == computer_choice:
    print("Both choice same: = game tie")

elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper covered Rock = computer wine")
    else:
        print("Rock smashes Scissor = You wine")


elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Scissor cut's Paper = Computer wine")
    else:
        print("Paper covered Rock = You wine")

elif user_choice == "Scissor":
    if computer_choice == "Rock":
        print("Rock Brocken Scissor = Computer wine")

    else:
        print("Paper cout of Scissor = You wine")

