def average_value_in_file(name):
    file = open(name)
    lines = file.readlines()
    value_sum = 0
    count = 0
    for line in lines:
        line = float(line)
        value_sum += line
        count += 1
    if count != 0:
        avg_value = value_sum / count
        return avg_value
    else:
        avg_value = 0.0
        return avg_value
