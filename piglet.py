import random

score = 0

def main():
    global score
    score = 0
    piglet()

def piglet():
    print("Welcome to Piglet!")
    dice_roll()

def dice_roll():
    roll = random.randint(1, 6)
    print("You rolled a", roll)
    global score
    if roll == 1:
        print("You got 0 points.")
    else: 
        score += roll
        decision = str(input("Roll again? "))
        decision = decision.casefold()
        if (decision == "yes") or (decision == "y"):
            dice_roll()
        elif (decision == "no") or (decision == "n"):
                print("You got", score, "points.")

main()
