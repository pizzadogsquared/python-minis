def sentinel_sum():
    added_num = 0
    resume = True
    while resume == True:
        to_add = int(input("Type a number: "))
        if to_add == -1:
            print("Sum is", added_num)
            resume = False
        else:
            added_num += to_add

sentinel_sum()
