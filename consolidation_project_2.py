# "Tuple Out" Dice Game (Code)
# Install dependenes if needed (conda install)

import os
import random

def rolling_dice():
    return [random.randint(1, 6) for _ in range(3)]

def score(dice):
    if len(set(dice)) == 1:
        return 0
    else:
        return sum(dice)
    
def main():
    print("Welcome to the 'Tuple Out' Dice Game!")
    while True:
        input("Press enter for rolling the dice.")
        dice = rolling_dice()