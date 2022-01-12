def merge_sort(items):
    if len(items) == 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    l, r = 0, 0
    while l < len(left) and r < len(right):
        items[l + r] = min(left[l], right[r])
        if left[l] < right[r]:
            l += 1
        else:
            r += 1
    while l < len(left):
        items[l + r] = left[l]
        l += 1
    while r < len(right):
        items[l + r] = right[r]
        r += 1
    return items


numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
merge_sort(numbers)
print(numbers)
