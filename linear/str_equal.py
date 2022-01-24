def str_equals(str_a, str_b):
    if len(str_a) != len(str_b):
        return False
    for i in range(len(str_a)):
        if str_a[i] != str_b[i]:
            return False
    return True


print(str_equals("Pam", "Jennifer"))
print(str_equals("Isabel", "Isador"))
print(str_equals("Peter", "Peter"))
