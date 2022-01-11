
def find_min(items):
    smallest = None
    for i in items:
        if smallest is None or i < smallest:
            smallest = i
    return smallest


numbers = [10, 24, 3, 67, 21, 9, 34]
print(find_min(numbers))
print(min(numbers))
