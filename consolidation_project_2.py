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

            if len(set(dice)) == 1:
                print("This is a tuple! You receive 0 points.")
            else:
                fixed_dice = set()
                while True:
                    choose = input("Do you want to re-roll any dice? (yes/no): ").lower()
                    if choose != 'yes':
                        break
                    else:
                        fixing_dice = input("Enter the dice you want to fix (1, 2, or 3), or input '0' to stop: ")
                        if fixing_dice == '0':
                            break
