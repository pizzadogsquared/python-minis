def caesar_cipher():
    new_phrase = ""
    phrase = str(input("Your message? "))
    phrase = phrase.upper()
    shift = int(input("Encoding key? "))
    for count in range(len(phrase)):
        letts = phrase[count]

        if letts == " ":
            new_phrase += " "

        elif letts == "\"":
            new_phrase += "\""

        elif letts == "\'":
            new_phrase += "\'"

        elif letts == "!":
            new_phrase += "!"

        else:
            new_phrase += chr((ord(letts) + shift - 65) % 26 + 65)

    print(new_phrase)

caesar_cipher()
