import random

choices = ["stone", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def check_winner(user, comp):
    if user == comp:
        return "Draw"
    elif (user == "stone" and comp == "scissors") or \
         (user == "scissors" and comp == "paper") or \
         (user == "paper" and comp == "stone"):
        return "You Win"
    else:
        return "Computer Wins"