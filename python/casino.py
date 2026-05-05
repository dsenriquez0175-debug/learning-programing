# import libraries or packages
from random import randint
import os

#Declare and initialize variables and/or constants
player_lives = 3
dice1 = 0
dice2 = 0
roll_count = 0
equal_count = 0
status = True 

# Functions
def roll_dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1, dice2

# Main
while status:
    os.system('cls')
    dices = roll_dices()
    roll_count+=1
    dices_add = 0
    print(f"#" * 20)
    print(f"Roll dice N° .: {roll_count}")
    print(f"#" * 20)
    print(f"player_lives: {player_lives}")
    print(f"Dice 1: {dices[0]}")
    print(f"Dice 2: {dices[1]}")
    dices_add = dices[0] + dices[1]

    if dices_add % 2 != 0:
        player_lives-=1
        print("you've lost one live ::: Now you have {player_lives}lives")
        if player_lives == 0:
            print("::: GAME OVER :::")
    print(f"Dices addition: {dices_add}")
    if roll_count == 5:
        break
    else:
        press_key = input("\n press any key to roll dices again")

