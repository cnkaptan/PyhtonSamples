def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    if aStr == '':
        return False
    elif len(aStr) == 1:
        return aStr == char
    else:
        i = int(len(aStr) / 2)
        middle = aStr[i]
        if middle == char:
            return True
        elif char < middle:
            return isIn(char, aStr[:i])
        else:
            return isIn(char, aStr[i:])

print(isIn('x', 'aaguuxy'))

