
def find_min(items):
    smallest = None
    for i in items:
        if smallest == None or i < smallest:
            smallest = i
    return smallest


print(find_min([10, 24, 3, 67, 21, 9, 34]))
print(min([10, 24, 3, 67, 21, 9, 34]))
