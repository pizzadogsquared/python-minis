def weather():
    name = str(input("Input file? "))
    file = open(name)
    for line in file:
        for numb in line.split():
            numb = float(numb)
            print(numb)
    
weather()
