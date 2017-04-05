from collections import Counter

def is_isogram(phrase):
    # strip away all non-alphabetical characters
    ph = ''.join(ch for ch in phrase if ch.isalpha())
    char_count = set(Counter(list(ph.lower())).values())
    # empty space is considered isogram
    # so char_count = 1 or 0 is an isogram
    
    # case of multiple occurrences of letters
    if len(char_count) > 1:
        return False
    # case of empty string as isogram
    elif len(char_count) == 0:
        return True
    # case of only doubled or tripled letters
    elif list(char_count)[0] != 1:
        return False
    else:
        return True