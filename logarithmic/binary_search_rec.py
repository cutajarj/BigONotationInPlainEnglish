def binary_search(items, x, start, end):
    mid = (start + end) // 2
    if start > end:
        return -1
    elif x > items[mid]:
        return binary_search(items, x, mid + 1, end)
    elif x < items[mid]:
        return binary_search(items, x, start, end - 1)
    else:
        return mid


arr = ["Bob", "Isabel", "James", "Pam", "Peter", "Ruth", "Sam", "Vera"]
print(binary_search(arr, "Isabel", 0, len(arr) - 1))
