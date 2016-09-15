"""
    functions are first class objects
        - have types
        - can be elements of data structures like lists
        - can appear in expressions
            - as part of an assignment statement
            - as an argument to a function
        - particularly useful to use functions as arguments when coupled with lists
"""


def applyToEach(L, f):
    """
        L is a list, f a function mutates(degismek) L by replacing each element,
        e, of L by f(e)
    """
    for i in range(len(L)):
        L[i] = f(L[i])


L = [1, -2, 3.4]

L1 = L.copy()
applyToEach(L1, abs)
print(L1)

L2 = L.copy()
applyToEach(L2, int)
print(L2)
print('------------------------------------------------------------')

testList = [1, -4, 8, -9]


def timesFive(a):
    return a * 5


applyToEach(testList, timesFive)
print(testList)

print('------------------------------------------------------------')


def applyFuns(L, x):
    for f in L:
        print(f(x), end=" ")


F = [abs, int, float]

applyFuns(F, -3.4)

print()

# map = the idea of apply something to a collection
for elt in map(abs, [1, -2, 3, -4]):
    print(elt, end=" ")

print()

L3 = [1, 28, 36]
L4 = [2, 57, 9]

for elt in map(min, L3, L4):
    print(elt, end=" ")
print()
print('------------------------------------------------------------')


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


def square(a):
    return a * a


def halve(a):
    return a / 2


def inc(a):
    return a + 1


print(applyEachTo([inc, square, halve, abs], -3))
print(applyEachTo([inc, square, halve, abs, int], 3.0))
