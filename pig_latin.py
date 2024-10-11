def pig_latin(name):
    file = open(name)
    for line in file:
        for word in line.split():
            if (word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u'):
                word += 'yay '
                print(word, end = '')
            else:
                count = len(word)
                new_word = word[1:count]
                new_word += word[0]
                new_word += 'ay '
                word = new_word
                print(word, end = '')
        print()
                
                
