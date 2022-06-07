import math


def merge(items, left, right):
    l, r = 0, 0
    for i in range(len(items)):
        value_l = left[l] if l < len(left) else math.inf
        value_r = right[r] if r < len(right) else math.inf
        items[i] = min(value_l, value_r)
        if value_l < value_r:
            l += 1
        else:
            r += 1
    return items


def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(items, left, right)


numbers = [5, 1, 3, 2, 4, 9, 6, 7, 8]
merge_sort(numbers)
print(numbers)
numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
merge_sort(numbers)
print(numbers)
