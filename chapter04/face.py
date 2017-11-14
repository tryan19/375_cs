from graphics import *


def main():
    win = GraphWin("Face Drawing", 400, 400)


    # Draw your face here!

    center = Point(100, 100)
    circle = Circle(center, 30)
    circle.setFill('blue')
    circle.draw(win)
    label = Text(center, "")
    label.draw(win)

    center= Point(100,100)
    circle = Circle(center, 20)
    circle.setFill('green')
    circle.draw(win)
    label = Text(center, "")
    label.draw(win)

    center = Point(200, 100)
    circle = Circle(center, 30)
    circle.setFill('red')
    circle.draw(win)
    label = Text(center, "")
    label.draw(win)

    center = Point(200, 100)
    circle = Circle(center, 20)
    circle.setFill('green')
    circle.draw(win)
    label = Text(center, "")
    label.draw(win)

    center = Point(200, 100)
    circle = Circle(center, 5)
    circle.setFill(color_rgb(0,0,0))
    circle.draw(win)
    label = Text(center, "")
    label.draw(win)

    center = Point(100, 100)
    circle = Circle(center, 5)
    circle.setFill(color_rgb(0,0,0))
    circle.draw(win)
    label = Text(center, "")
    label.draw(win)







    input("Press any key to quit")


main()


