# import libraries or packages
from random import randint
import os

#Declare and initialize variables and/or constants
player_lives = 3
dice1 = 0
dice2 = 0
roll_count = 0
equal_count = 0
dices_add = 0
acum_dices = 0
status = True 
player_lives = 3

# Functions
def roll_dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1, dice2

# Main
print(":::WELCOME TO CASINO:::")
press_key = input("\npress any key to start the game:::")
while status:
    os.system('cls')
    dices = roll_dices()
    roll_count+=1
    dices_add = 0
    print(f"#" * 20)
    print(f"Roll dice N° .: {roll_count}")
    print(f"#" * 20)
    print(f"player_lives: {player_lives}")

    if acum_dices > 14:
        dicex = dices[randint(0, 1)]
        print(f"Dice: {dicex}")
        acum_dices += dicex
    else:
        print(f"Dice 1: {dices[0]}")
        print(f"Dice 2: {dices[1]}")
        dices_add = dices[0] + dices[1]
        acum_dices += dices_add

    if acum_dices >=20:
        print(":::CONGRATULATIONS, YOU' VE WIN:::")

    if dices_add % 2 != 0:
        player_lives-=1
        print("you've lost one live ::: Now you have {player_lives}lives")
        if player_lives == 0:
            print("::: GAME OVER :::")
            break
    
    if (dices[0] == 6 and dices[1] == 6) or (dices[0] == 1 and dices[1] == 1)
    player_lives +=1
    print("you've win a live :::")

    print(f"dices addition (current roll): {dices_add}")
    print(f"dices acum: {acum_dices}")

    print(f"dices addition: {dices_add}")

    if player_lives == 0:
        print(":::game over:::")
        print(f"total roll count: {roll_count}")
        break

    print(f"Dices addition: {dices_add}")
    if roll_count == 5:
        break
    else:
        press_key = input("\n press any key to roll the dices again")

