def number_square(min_value, max_value):
    my_range = max_value - min_value + 1

    for rows in range(my_range):
        for columns in range(my_range):
            index = rows + columns
            print(index % my_range + min_value, end = "")
        print()

