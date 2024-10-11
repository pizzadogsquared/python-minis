# Print a delicious donut.
# Looks like:
#     XXXXX
#  XXXXXXXXXXX
#  XXXXX XXXXX
# XXXX     XXXX
# XXXX     XXXX
#  XXXXX XXXXX
#  XXXXXXXXXXX
#     XXXXX
#

FILLING = "X"

def donut():
    for i in range(1, 2):
        print("    ", FILLING * 5)
        print (" ", FILLING * 11)
        print(" ", FILLING * 5, FILLING * 5)
        print("", FILLING * 4, "   ", FILLING * 4)
    other_half()

def other_half():
    for i in range(1, 2):
        print("", FILLING * 4, "   ", FILLING * 4)
        print(" ", FILLING * 5, FILLING * 5)
        print (" ", FILLING * 11)
        print("    ", FILLING * 5)
        
donut()
