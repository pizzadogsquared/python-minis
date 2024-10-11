def is_palindrome(string):
    newstring1 = ""
    newstring2 = ""
    string = string.lower()
    for i in range(len(string)):
        newstring1 += string[i]
        newstring2 += string[(abs(i+1))*-1]
    print(newstring1)
    print(newstring2)

is_palindrome(" !  ")
is_palindrome("banana")    
is_palindrome("she sells seashells")
