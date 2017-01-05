#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
    what = what.strip() # Get rid of leading / trailing whitespace
    if not what:    # If what is empty
        return 'Fine. Be that way!'
    elif what.isspace():
        return 'Fine. Be that way!' # If what only contains whitespace
    elif what.isupper():
        return 'Whoa, chill out!' # Uppercase = yelling
    elif what[-1] == '?': # Ends with question mark
        return 'Sure.'
    else:
        return 'Whatever.'