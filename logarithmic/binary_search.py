def binary_search(items, x):
    start = 0
    end = len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if x > items[mid]:
            start = mid + 1
        elif x < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


names = ["Bob", "Isabel", "James", "Pam", "Peter", "Ruth", "Sam", "Vera"]
print(binary_search(names, "James"))
