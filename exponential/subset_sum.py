def subset_sum(s, target):
    n = len(s)
    for i in range(2 ** n):
        print("[ ", end='')
        sum = 0
        for j in range(n):
            if i & (2 ** j):
                sum += s[j]
                print(s[j], " ", end='')
        print("] sum = ", sum)
        if sum == target:
            return True
    return False


print(subset_sum([2, 3, 5, 7, 11, 15], 14))
# print(subset_sum([2, 3, 5, 7, 11, 15], 6))
