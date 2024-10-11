def stutter(phrase):
    amt_letts = len(phrase)
    new_phrase = ""
    for count in range(0, amt_letts):
        new_phrase += 2 * phrase[count]
    return new_phrase

