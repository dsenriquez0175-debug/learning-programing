from random import randint

status = true
count = 0 
# Functions
def roll_dices():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1, dice2

dices = roll_dices()
print(dices)
print(f"Dice 1: {dices[0]}")
print(f"Dice 2: {dices[1]}")

if (dices[0] == dices[1]):
    print("you ve win")
    break
else:
    print("Try again !!!")
    key= input ("press any key to roll_dices")
