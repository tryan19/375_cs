from graphics import *


def main():
    win = GraphWin("Face Drawing", 400, 400)


    # Draw your face here!
    size = eval(input("How big do you want to make the window? "))

    win = GraphWin("Scaling Example", size, size)
    win.setCoords(0, 0, 10, 10)

    rectangle = Rectangle(Point(2.1, 1), Point(2, 8))
    rectangle.setFill('yellow')
    rectangle.setOutline('black')
    rectangle.draw(win)

    rectangle = Rectangle(Point(2.1, 1.1), Point(8, 1))
    rectangle.setFill('yellow')
    rectangle.setOutline('black')
    rectangle.draw(win)

    rectangle = Rectangle(Point(8, 8), Point(8.1, 1))
    rectangle.setFill('yellow')
    rectangle.setOutline('black')
    rectangle.draw(win)

    rectangle = Rectangle(Point(2, 8), Point(8.1, 8.1))
    rectangle.setFill('yellow')
    rectangle.setOutline('black')
    rectangle.draw(win)

    center = Point(.5, 9.2)
    circ = Circle(center, 1.1)
    circ.setFill(color_rgb(255,165,0))
    circ.draw(win)

    line = Line(Point(3, 1.1), Point(3, 3))
    line.draw(win)


    line = Line(Point(3, 3), Point(4, 3))
    line.draw(win)

    line = Line(Point(4, 1.1), Point(4, 3))
    line.draw(win)

    center = Point(3.2, 2)
    circ = Circle(center, .1)
    circ.setFill(color_rgb(0,0,0))
    circ.draw(win)

    rectangle = Rectangle(Point(0, 0), Point(10, 1))
    rectangle.setFill('green')
    rectangle.setOutline('green')
    rectangle.draw(win)

    polygon = Polygon (Point(2, 8.1) , Point(5, 10)  , Point(8.1,8.1))
    polygon.draw(win)
    polygon.setFill('blue')










    input("Press any key to quit")


main()


