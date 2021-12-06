import math
from math import dist


def find_closest_pair(points):
    minimum_dist = math.inf
    closest_pair = (None, None)
    for i in range(len(points)):
        for j in range(len(points)):
            distance = dist(points[i], points[j])
            if i != j and distance < minimum_dist:
                closest_pair = (points[i], points[j])
                minimum_dist = distance
    return closest_pair


inputs = [(10,10), (100,120), (50, 21), (100, 10), (60, 35), (65, 36)]
print(find_closest_pair(inputs))
