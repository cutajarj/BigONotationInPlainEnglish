
def number_of_edges(nodes):
    result = 0
    for i in range(nodes):
        for j in range(i, nodes - 1):
            result += 1
    return result


print(number_of_edges(6))
