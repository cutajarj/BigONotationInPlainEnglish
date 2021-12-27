
def number_of_edges(nodes):
    result = 0
    for i in range(nodes):
        result += nodes - 1 - i
    return result


print(number_of_edges(6))
