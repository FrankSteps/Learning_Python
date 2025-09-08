#jokenpo - The Game

# rules:
#   paper -> rock
#   rock -> Scissors
#   Scissors -> paper

#import libraries
import random
import sys

round = 0

# points
point_user = 0
point_soft = 0

# Only 3 rounds between you and the software
while round < 3:
    # software choice
    jokenpo = ["paper", "rock", "scissors"] 
    random_jokenpo = random.choice(jokenpo) 

    # user choice
    user_jokenpo = input("chose: paper, rock or scissors: ").lower() 

    # display software choice
    print("Software chose:", random_jokenpo) 
    round += 1 

    # just paper, rock and scissors are valid values
    if user_jokenpo != "paper" and user_jokenpo != "rock" and user_jokenpo != "scissors": 
        sys.exit(1)

    # game conditions
    if user_jokenpo == random_jokenpo:
        print("tie :(")

    # paper hit rock
    elif user_jokenpo == "paper" and random_jokenpo == "rock":
        print("user win")
        point_user += 1

    # rock hit scissors
    elif user_jokenpo == "rock" and random_jokenpo == "scissors":
        print("user win")
        point_user += 1
    
    # scissors hit paper
    elif user_jokenpo == "scissors" and random_jokenpo == "paper":
        print("user win")
        point_user += 1

    # points for the software if the winning option is theirs
    else:
        print("Software win")
        point_soft += 1

# Whon won?
if point_user > point_soft:
    print("You WIN!!!")

elif point_user == point_soft:
    print("Tie...")
    
else:
    print("You lose... better luck next time!")
