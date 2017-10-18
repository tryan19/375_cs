#guessing-game.py
#this program gives you a number that you have to guess
#By: Tom Ryan

import random
def main():
    magic_number= random.randrange(1,101)
    guess = 0
    attempts = 0
    while guess != magic_number:
        guess=eval(input("What is your guess"))
        if guess < magic_number:
            print("too low")
        elif guess > magic_number:
            print("too high")

        attempts = attempts + 1

    print("You win! It took you" , attempts, "tries.")

main()
