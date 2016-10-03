listSample = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5];

listSample2 = [1, 'a', ['cat'], 2]


def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    # print("Answer 1")
    # if aList == []:
    #     return aList
    # if isinstance(aList[0], list):
    #     return flatten(aList[0]) + flatten(aList[1:])
    # return aList[:1] + flatten(aList[1:])

    # print("Answer 2")
    # ret = []
    # for i in aList:
    #     if isinstance(i, list) or isinstance(i, tuple):
    #         ret.extend(flatten(i))
    #     else:
    #         ret.append(i)
    # return ret

    # print("Answer 3")
    t = []
    for i in aList:
        if not isinstance(i, list):
            t.append(i)
        else:
            t.extend(flatten(i))
    return t


print(flatten(listSample))

print('------------------------------------------------------------')


def f(i):
    return i + 2


def g(i):
    return i > 5


def applyF_filterG(L, f, g):
    copyList = L[:]

    for num in copyList:
        if not g(f(num)):
            if num in L:
                L.remove(num)
    if len(L) == 0:
        max = -1
    else:
        max = L[0]

        for item in L:
            if item > max:
                max = item
    return max


L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print('------------------------------------------------------------')

d1 = {1: 30, 2: 20, 3: 30, 5: 80}
d2 = {1: 40, 2: 50, 3: 60, 4: 70, 6: 90}
d3 = {1: 30, 2: 20, 3: 30}
d4 = {1: 40, 2: 50, 3: 60}


def f(a, b):
    return a + b


def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # print("My Solution 11/20")
    # print(d1.keys())
    # print(d2.keys())
    # interKeys = set(d1.keys() & d2.keys())
    # unionKeys = set(d1.keys() | d2.keys())
    # differKeys = unionKeys.difference(interKeys)
    # print(interKeys)
    # print(differKeys)
    # interMap = {}
    # differMap = {}
    #
    # for key in interKeys:
    #     interMap[key] = f(d1[key], d2[key])
    # for key in differKeys:
    #     differMap[key] = f(d1.get(key,0), d2.get(key,0))
    #
    # return (interMap, differMap)

    # print("Correct Answer 20/20")
    # symmetric difference, keys in either d1 or d2 but not both.
    sym_diff = d1.keys() ^ d2.keys()
    print(sym_diff)
    # intersection, keys that are common to both d1 and d2.
    intersect = d1.keys() & d2.keys()
    print(intersect)
    # apply f on values of the keys that common to both dicts.
    a = {k: f(d1[k], d2[k]) for k in intersect}
    # add key/value pairings from d1 and d2 using keys that appear in sym_diff
    b = {k: d1[k] for k in sym_diff & d1.keys()}
    b.update({k: d2[k] for k in sym_diff & d2.keys()})
    return a, b


# print(dict_interdiff({1: 1, 2: 2, 3: 3, 4: 5, 8: 4, 10: 0}, {9: 1, 5: 3, 6: 3, 7: 4}))
print(dict_interdiff(d1,d2))
print('------------------------------------------------------------')

L = [[1, 2], [3, 4], [5, 6, 7]]


def deep_reverse(L):
    L.reverse()
    for item in L:
        if type(item) == list:
            item.reverse()
    print(L)


deep_reverse(L)

print('------------------------------------------------------------')


def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''

    L = []
    # if base >= num:
    #     return 0
    # elif base ** 2 >= num:
    #     return 2
    # else:
    #     exponent = 3
    #     while True:
    #         if base ** exponent > num:
    #             return exponent - 1
    #         else:
    #             exponent += 1

    exponent = 0
    while True:
        result = base ** exponent
        if result == num:
            return exponent
        else:
            L.append(exponent)
            if result > num:
                break
            else:
                exponent += 1

    closestPower = 0
    min_difference = abs(num - base ** L[0])

    for index in range(1, len(L), 1):

        difference = abs(num - base ** L[index])
        if difference < min_difference:
            min_difference = difference
            closestPower = L[index]

    return closestPower


print(closest_power(16, 136))
