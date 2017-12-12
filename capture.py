# animate_with_keys.py
#
# This program illustrates how to animate a drawing using input from the keyboard.
#
# by Mr. Ciccolo

from graphics import *
from random import *
from math import *


def main():
    print("Press the arrow keys to move the white circle, press 'q' to quit")
    score = 0
    timer = 60

    window_size = 600
    canvas_size = 20

    win = GraphWin("Animation Example with Keyboard", window_size, window_size)
    win.setCoords(0, 0, canvas_size, canvas_size)
    win.setBackground("black")

    score_text = Text(Point(2,18),"Score:0")
    score_text.setFill("white")
    score_text.draw(win)
    score_text.setFace("courier")
    score_text.setSize(25)

    time_text = Text(Point(18,18),"Timer:60")
    time_text.setFill("white")
    time_text.draw(win)
    time_text.setFace("courier")
    time_text.setSize(25)


    circle = Circle(Point(canvas_size / 2, canvas_size / 2), 2)
    circle.setFill("white")
    circle.draw(win)

    pellet = Circle(Point(0,0), 1)
    pellet.setFill("yellow")
    pellet.draw(win)
    move_to_random_point(pellet, canvas_size)

    time_check = time.time()

    message_text = Text (Point(canvas_size/2, canvas_size /2), "CLICK TO START")
    message_text.setTextColor("red")
    message_text.draw(win)
    message_text.setFace("courier")
    message_text.setSize(30)
    message_text.setText("")

    while timer > 0:
        key = win.checkKey()

        delta_x = 0
        delta_y = 0

        if key == "q":
            break
        elif key == "Up":
            delta_y += 1
        elif key == "Down":
            delta_y -= 1
        elif key == "Left":
            delta_x -= 1
        elif key == "Right":
            delta_x += 1

        circle.move(delta_x, delta_y)

        if collide(circle, pellet):
            move_to_random_point(pellet, canvas_size)
            score += 1
            score_text.setText("score:" + str(score))
        if time.time() - time_check > 1 :
            timer -= 1
            time_check = time.time()
            time_text.setText("Time:" + str(timer))

def collide(c1, c2):
    a = c1.getCenter().getX() - c2.getCenter().getX()
    b = c1.getCenter().getY() - c2.getCenter().getY()
    c = sqrt(a**2 + b**2)
    return c <= (c1.getRadius() + c2.getRadius())


def move_to_random_point(circle, bounds):
    next_x = randrange(circle.getRadius(), bounds + 1 - circle.getRadius())
    next_y = randrange(circle.getRadius(), bounds + 1 - circle.getRadius())

    current_x = circle.getCenter().getX()
    current_y = circle.getCenter().getY()

    delta_x = next_x - current_x
    delta_y = next_y - current_y

    circle.move(delta_x, delta_y)




main()
