# a.
print("a.")
maxs = 4
n = 0
while n <= maxs:
    n += 1
    print(n)
print()

# b.
print("b.")
total = 25
number = 0
while number <= total // 5 + 1:
    number += 1
    total = total - number
    print(total, number)
print()

# c.
print("c.")
i = 0
while i <= 1:
    i += 1
    j = 0
    while j <= 2:
        j += 1
        k = 0
        while k <= 3:
            k+= 1
            print("*", end="")
        print("!", end="")
    print()
print("\t    \t")
