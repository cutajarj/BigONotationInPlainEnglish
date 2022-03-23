from itertools import takewhile
from math import dist


def find_closest_pair(points):
    sorted_by_x = sorted(points, key=lambda p: p.x)
    sorted_by_y = sorted(points, key=lambda p: p.y)
    delta_pair = find_closest_pair_rec(sorted_by_x, sorted_by_y)
    return delta_pair[1], delta_pair[2]


def find_closest_pair_rec(points_by_x, points_by_y):
    if len(points_by_x) == 1:
        return float('inf'), points_by_x[0], points_by_x[0]
    if len(points_by_x) == 2:
        return dist(points_by_x[0], points_by_x[1]), points_by_x[0], points_by_x[1]
    mid = len(points_by_x) // 2
    left_by_x, right_by_x = points_by_x[:mid], points_by_x[mid:]
    mid_x = right_by_x[0].x
    left_by_y, right_by_y = [p for p in points_by_y if p.x < mid_x], [p for p in points_by_y if p.x >= mid_x]
    delta_pair = min(find_closest_pair_rec(left_by_x, left_by_y), find_closest_pair_rec(right_by_x, right_by_y),
                     key=lambda pair: pair[0])
    points_boundary_by_y = [p for p in points_by_y if mid_x - delta_pair[0] <= p.x <= mid_x + delta_pair[0]]
    for p in range(len(points_boundary_by_y) - 1):
        current = points_boundary_by_y[p]
        pts_in_2x_delta_box = list(takewhile(lambda j: j.y <= current.y + delta_pair[0], points_boundary_by_y[p + 1:]))
        if len(pts_in_2x_delta_box) > 0:
            min_delta_in_box = min([(dist(points_boundary_by_y[p], d), points_boundary_by_y[p], d)
                                    for d in pts_in_2x_delta_box], key=lambda pair: pair[0])
            delta_pair = min(min_delta_in_box, delta_pair, key=lambda pair: pair[0])
    return delta_pair


