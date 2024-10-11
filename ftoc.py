# converts Fahrenheit temperatures to Celsius
def ftoc(tempf, tempc):
    tempc = (tempf - 32) * (5 / 9)

def main():
    tempf = 98.6
    tempc = 0.0
    ftoc(tempf, tempc)
    print("Body temp in C is:", tempc)

main()
