def print_strings(letts, num):
    space = " "
    for i in range(num, num + 1):
        print((letts + space)* i, end=" ")

print_strings("abc", 5)
