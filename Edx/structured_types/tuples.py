"""
    an ordered sequence of elements , can mix element types
    immutable, can not changes elements values
    represent with parenthesss
"""

te = ()
tup1 = (5)
print(tup1)
print(type(tup1))

tup2 = (5,)
print(tup2)
print(type(tup2))

t = (2, 'one', 3)
print(t[0])

t = t + (5, 6)
print(t)

print(t[1:2])  # ('one',) sana tuple doner , bunu da ',' den anlariz
print(t[1])

print(t[1:3])


# t[1] = 4 # gives error , cant modify object , tuples are immutable


def getData(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_num = min(nums)
    max_num = max(nums)
    unique_words = len(words)
    return (min_num, max_num, unique_words)


k = (small, large, words) = getData(((1, 'mine'),
                                     (3, 'yours'),
                                     (5, 'ours'),
                                     (7, 'mine')))
print(small, large, words)
print(k)

x = (1, 2, (3, 'John', 4), 'Hi')
print(x[0])
print(x[2])
print(x[-1])
print(x[2][2])
print(x[2][-1])
print(x[-1][-1])
print(x[0:1])
print(x[0:-1])
print(len(x))
print(2 in x)
print(3 in x)

def oddTuples(aTup):
    newTuple = ()
    for element in aTup:
        if type(element) == str:
            if len(element) % 2 == 1:
                newTuple += (element,)
        else:
            if element %2 == 1:
                newTuple += (element,)
    return newTuple

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
print(oddTuples(('I', 'am', 3, 4, 'tuple',7)))