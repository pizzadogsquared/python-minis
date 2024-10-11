def is_palindrome(phrase):
    phrase = phrase.casefold()
    amt_letts = len(phrase)
    new_phrase = ""
    for count in range(0, amt_letts):
        new_phrase += phrase[amt_letts - 1 - count]
    if phrase == new_phrase:
        return True
    else:
        return False

