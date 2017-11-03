#pig.py
#
#This is program that plays the game PIG
#The game is played between 2 players
#During each players turn they can roll as long as they want, but if they roll a 1 they bust
#If they bust they get 0 points for the round
#At any time a player can decide to hold (stop rolling)
#The added total of rolls for each player is added to the player's scores
#
#by:Tom, Ben, and Becca


import random

player1 = 0
player2 = 0
score1 = 0
score2 = 0


def main():
    global player1, player2, score1, score2
    display_welcome ()
    print() #blank line for spacing
    player1 = input("What is the name of player 1?")
    player2 = input("What is the name of player 2?")
    print()
    next_turn = 1

    while score1 < 100 and score2 < 100 :
        scoreboard()

        if next_turn == 1:
            print()
            print(player1, "it is your turn.")
            points = play_turn()
            score1 = score1 + points
            print()
            next_turn = 2
        else:
            print()
            print(player2, "it is your turn.")
            points = play_turn()
            score2 = score2 + points
            print()
            next_turn = 1

    if score1 >= 100:
        print("Congradulations", player1, "won!")
        print("Game Over")
    else:
        print("Congradulations", player2, "won!")
        print("Game Over")




def display_welcome():
    print(" .----------------.  .----------------.  .----------------.")
    print("| .--------------. || .--------------. || .--------------. |")
    print("| |   ______     | || |     _____    | || |    ______    | |")
    print("| |  |_   __ \   | || |    |_   _|   | || |  .' ___  |   | |")
    print("| |    | |__) |  | || |      | |     | || | / .'   \_|   | |")
    print("| |    |  ___/   | || |      | |     | || | | |    ____  | |")
    print("| |   _| |_      | || |     _| |_    | || | \ `.___]  _| | |")
    print("| |  |_____|     | || |    |_____|   | || |  `._____.'   | |")
    print("| |              | || |              | || |              | |")
    print("| '--------------' || '--------------' || '--------------' |")
    print("'----------------'  '----------------'  '----------------'")
    print("")
    print("Welcome to Pig! You need 100 points to win.")

def scoreboard():
    print ("Scoreboard")
    print("----------")
    print(player1, ":" , score1)
    print(player2, ":" , score2)


def roll_dice():
        die = random.randrange(1, 7)
        print()
        print(" +---+ ")
        print(" |", die, "|")
        print(" +---+ ")
        print()

        return die


def play_turn():
    print("Press enter to roll dice")
    play_again = ""
    points = 0

    while play_again == "":
        roll = roll_dice()
        if roll == 1:
            points = 0
            input ("You busted! Press enter to continue.") #Input is to pause game
            play_again = 0
        else:
            points = roll + points
            print ("Your score is " ,points, ".", sep="")
            play_again = input("Press enter to roll dice or 'H' to hold")

    return points


main()
