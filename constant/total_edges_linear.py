
def number_of_edges(nodes):
    result = 0
    for i in range(nodes):
        result += nodes - (i + 1)
    return result


print(number_of_edges(1))
print(number_of_edges(2))
print(number_of_edges(3))
print(number_of_edges(4))
print(number_of_edges(5))
print(number_of_edges(6))
