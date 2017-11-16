from graphics import *


def main():
    win = GraphWin("Face Drawing", 400, 400)


    # Draw your face here!
    size = eval(input("How big do you want to make the window? "))

    win = GraphWin("Scaling Example", size, size)
    win.setCoords(0, 0, 10, 10)

    rectangle = Rectangle(Point(2.1, 3), Point(2, 8))
    rectangle.setFill('yellow')
    rectangle.setOutline('black')
    rectangle.draw(win)









    input("Press any key to quit")


main()


