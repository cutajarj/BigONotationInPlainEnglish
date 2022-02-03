import math
from math import dist

from quadratic.Point2D import Point2D


def find_closest_pair(points):
    minimum_dist = math.inf
    closest_pair = (None, None)
    for i in range(len(points)):
        for j in range(len(points)):
            distance = dist(points[i], points[j])
            if distance < minimum_dist and i != j:
                minimum_dist = distance
                closest_pair = (points[i], points[j])
    return closest_pair


# inputs = [Point2D(10, 10), Point2D(100, 120), Point2D(50, 21), Point2D(100, 10), Point2D(60, 35), Point2D(65, 36)]
# print(find_closest_pair(inputs))
