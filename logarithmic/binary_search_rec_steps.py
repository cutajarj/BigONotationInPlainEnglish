def binary_search(items, x, start, end):
    input("Searching for " + x + " in " + str(items[start:end+1]))
    mid = (start + end) // 2
    input("Middle point is " + items[mid])
    if start > end:
        input(x + "not found")
        return -1
    elif x > items[mid]:
        input(x + " is greater than " + items[mid])
        return binary_search(items, x, mid + 1, end)
    elif x < items[mid]:
        input(x + " is less than " + items[mid])
        return binary_search(items, x, start, mid - 1)
    else:
        print(x + " was found at position " + str(mid))
        return mid


names = ["Bob", "Isabel", "James", "Pam", "Peter", "Rose", "Sam", "Vera", "Zoe"]
print(binary_search(names, "Rose", 0, len(names) - 1))
