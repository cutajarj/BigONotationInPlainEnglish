import random

from graphics import *
from quadratic.Point2D import Point2D
from quadratic.closest_pair import find_closest_pair

WIDTH = 1728
HEIGHT = 972


def draw_points(points):
    win = GraphWin('Radar', WIDTH, HEIGHT)
    win.setBackground("black")
    for p in points:
        draw_point(p, win)

    rect = Rectangle(Point(1600, 900), Point(1680, 935))
    rect.setFill("blue")
    rect.draw(win)

    while True:
        click = win.getMouse()
        if 1600 <= click.getX() <= 1680 and 900 <= click.getY() <= 935:
            rect = Rectangle(Point(1600, 900), Point(1680, 935))
            rect.setFill("red")
            rect.draw(win)
            start = time.time()
            pair = find_closest_pair(points)
            end = time.time()
            rect = Rectangle(Point(1600, 900), Point(1680, 935))
            rect.setFill("blue")
            rect.draw(win)
            print("Time Taken: ", (end - start))
            draw_point(pair[0], win, "red")
            draw_point(pair[1], win, "red")
            circle_around(pair[0], pair[1], win)
        else:
            win.close()
            break


def circle_around(p1, p2, win):
    mid_point = Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
    circle = Circle(mid_point, 15)
    circle.setOutline("red")
    circle.setWidth(2)
    circle.draw(win)
    circle = Circle(mid_point, 25)
    circle.setOutline("red")
    circle.setWidth(3)
    circle.draw(win)


def draw_point(p, win, colour="green"):
    circle = Circle(Point(p.x, p.y), 3)
    circle.setFill(colour)
    circle.draw(win)


inputs = []
is_empty = [[True] * (HEIGHT + 1) for i in range(WIDTH + 1)]
#points_to_generate = 16000
#points_to_generate = 8000
#points_to_generate = 4000
points_to_generate = 400
while points_to_generate > 0:
    x, y = random.randrange(WIDTH), random.randrange(HEIGHT)
    if is_empty[x][y]:
        inputs.append(Point2D(x,y))
        is_empty[x][y] = False
        is_empty[x + 1][y] = False
        is_empty[x - 1][y] = False
        is_empty[x][y + 1] = False
        is_empty[x][y - 1] = False
        points_to_generate -= 1

draw_points(inputs)
