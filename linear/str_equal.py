def str_equal(str_a, str_b):
    if len(str_a) != len(str_b):
        return False
    for i in range(len(str_a)):
        if str_a[i] != str_b[i]:
            return False
    return True


print(str_equal("Isabel", "James"))
print(str_equal("Isabel", "Isador"))
print(str_equal("Isabel", "Isabel"))

