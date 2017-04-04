from collections import Counter

def is_isogram(phrase):
    # strip away all non-alphabetical characters
    phrase = ''.join(ch for ch in phrase if ch.isalpha())
    # empty space is considered isogram, so len is > 1, not == 1
    # this would not catch the case where all letters are only doubled, 3x etc
    if len(set(Counter(list(phrase.lower())).values())) > 1:
        return False
    else:
        return True