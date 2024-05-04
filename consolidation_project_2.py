# "Tuple Out" Dice Game (Code)
# Install dependenes if needed (conda install)

import random
import os

def rolling_dice():
    """Roll three dice and return the result."""
    return [random.randint(1, 6) for _ in range(3)]

def score(dice):
    """Calculate the score based on the rolled dice."""
    if len(set(dice)) == 1:  
        return 0
    else:
        return sum(dice)

def main():
    print("Welcome to the 'Tuple Out' Dice Game! There will be two rounds!")
    print("You lose if you have three of the same number.")
    print("Do not re-roll any dice that are of the same number.")
    players_number = int((input("Enter number of players: ")))
    scores = [0] * players_number
    rounds = 0
    while rounds < 2:
        for player in range(players_number):
            print(f"Player {player + 1}'s turn:")
            turn = 0
            dice = rolling_dice()
            print("You rolled: ", dice)
