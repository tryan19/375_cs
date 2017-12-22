# capture_the_pellets.py
#
# This program is a simple game called "Capture the Pellets!". The user moves a large white ball around the screen
# using the arrow keys to "capture" a small, randomly-placed, yellow pellet. They also can get a blue pellet that
# is worth five points and is also on the screen.  The program keeps track of the score and a
# countdown timer it also keeps track of the high score. The goal is to capture as many pellets as possible before time expires.
#
# by Tom Ryan

from graphics import *
from math import *
from random import *


def main():
    print("Press the arrow keys to move the white ball and capture the yellow pellets. Press 'q' to quit.")

    score = 0
    timer = 60

    file = open("chapter04/highscore.txt", "r")
    highscore = eval(file.read())

    window_size = 600
    canvas_size = 20

    win = GraphWin("Capture the Pellets!", window_size, window_size)
    win.setCoords(0, 0, canvas_size, canvas_size)
    win.setBackground("pink")

    score_text = Text(Point(0.2 * canvas_size, 0.9 * canvas_size), "Score: " + str(score))
    score_text.setTextColor("black")
    score_text.setFace("courier")
    score_text.setSize(24)
    score_text.draw(win)

    Highscore_text = Text(Point(0.5 * canvas_size, 0.9 * canvas_size), ("High score: " + str(highscore)))
    Highscore_text.setTextColor("black")
    Highscore_text.setFace("courier")
    Highscore_text.setSize(24)
    Highscore_text.draw(win)

    timer_text = Text(Point(0.8 * canvas_size, 0.9 * canvas_size), "Time: " + str(timer))
    timer_text.setTextColor("black")
    timer_text.setFace("courier")
    timer_text.setSize(24)
    timer_text.draw(win)

    message_text = Text(Point(canvas_size / 2, canvas_size / 2), "CLICK TO START")
    message_text.setTextColor("blue")
    message_text.setFace("courier")
    message_text.setSize(36)
    message_text.draw(win)

    win.getMouse()
    message_text.setText("")

    ball = Circle(Point(canvas_size / 2, canvas_size / 2), 2)
    ball.setFill("white")
    ball.draw(win)

    pellet = Circle(Point(0, 0), 1)
    pellet.setFill("yellow")
    pellet.draw(win)
    move_to_random_point(pellet, canvas_size)

    special_pellet = Circle(Point(0, 0), 1)
    special_pellet.setFill(color_rgb(127,255,212))
    special_pellet.draw(win)
    move_to_random_point(special_pellet, canvas_size)

    time_check = time.time();
    while timer > 0:
        key = win.checkKey()


        delta_x = 0
        delta_y = 0

        if key == "q":
            break
        elif key == "Up":
            delta_y = 1
        elif key == "Down":
            delta_y = -1
        elif key == "Left":
            delta_x = -1
        elif key == "Right":
            delta_x = 1

        ball.move(delta_x, delta_y)

        if collide(ball, pellet):
            score += 1
            score_text.setText("Score: " + str(score))
            move_to_random_point(pellet, canvas_size)

        if collide(ball, special_pellet):
            score +=5
            score_text.setText("Score:" + str(score))
            move_to_random_point(special_pellet, canvas_size)

        if score > highscore:
            highscore = score
            Highscore_text.setText("High score: " + str(highscore))

        if (time.time() - time_check) > 1:
            time_check = time.time()
            timer -= 1
            timer_text.setText("Time: " + str(timer))





    message_text.setTextColor("blue")
    message_text.setText("GAME OVER")

    file = open("chapter04/highscore.txt", "w")
    file.write(str(highscore))
    file.close()

    input("Game over! Your final score was " + str(score) + ". Press Enter to quit.")


def collide(c1, c2):
    # Calculate the distance between the center points of the circles using Pythagorean theorem (a^2 + b^2 = c^2)
    a = c1.getCenter().getX() - c2.getCenter().getX()
    b = c1.getCenter().getY() - c2.getCenter().getY()
    distance = sqrt(a**2 + b**2)

    collision = distance <= (c1.getRadius() + c2.getRadius())

    return collision


def move_to_random_point(circle, bounds):
    current_x = circle.getCenter().getX()
    current_y = circle.getCenter().getY()

    next_x = randrange(circle.getRadius(), bounds + 1 - circle.getRadius())
    next_y = randrange(circle.getRadius(), bounds + 1 - circle.getRadius())

    delta_x = next_x - current_x
    delta_y = next_y - current_y

    circle.move(delta_x, delta_y)


main()
