L = [2, 1, 3]
print(L)
# add elements end of the list
L.append(5)  # actually changed L itself
print(L)

# Lists are python objects, everything in Python is an object


# to combine lists together use concatenation , + operator

L1 = [2, 1, 3]
L2 = [4, 5, 6]
L3 = L1 + L2
print(L3)

L1.extend([0, 6])
print(L1)
print('------------------------------------------------------------')
# delete element at a specific index with del(L[index])
print(L3)
del (L3[1])
print(L3)

# remove element at end of list with L.pop() returns to removed element

element = L3.pop()
print(element, L3)

"""
    remove a specific element with L.remove(element)
        - looks for element and removes it
        - if element occurs multiple times, removes first occurence
        - if element not in list, gives an error
"""
print('------------------------------------------------------------')
L4 = [2, 1, 3, 6, 3, 7, 0]
print(L4)
L4.remove(2)
print(L4)
L4.remove(3)
print(L4)
del (L4[1])
print(L4)
element = L4.pop()
print(element, L4)

print('------------------------------------------------------------')

"""
    convert string to list with list(s), returns a list with every character from s an element in L

    can use s.split(), to split a string on character parameter, splits on spaces if called without a parameter

    use ''.join(L) to turn a list of characters into a string, can give a character in quotes to add char between every element

"""
s = 'I <3 cs'
L5 = list(s)
print(L5)
L6 = s.split('<')
print(L6)
L7 = s.split()  # default space
print(L7)

L8 = ['a', 'b', 'c']
s1 = ''.join(L8)
print(s1)
s2 = '_'.join(L8)
print(s2)

print('------------------------------------------------------------')

L9 = [9, 6, 0, 3]

L10 = sorted(L9)  # return sorted list, does not mutate list
print('L9:', L9)
print('L10', L10)

L9.sort()  # L9 uzerinde degisti
print(L9)
L9.reverse()
print(L9)

print('------------------------------------------------------------')

L10 = [1, 2, 3, 4]
L11 = [1, 2, 5, 6]

# burada sikinti ilk element silindigi zaman listenin sizi degisecek 1. indexteki artik 3 olacak o yuzden 2 yi direk atliyor
def remove_dubs(listA, listB):
    for e in listA:
        print(e)
        if e in listB:
            listA.remove(e)

def remove_dubs_new(listA, listB):
    listA_copy = listA[:]
    for e in listA_copy:
        print(e)
        if e in listB:
            listA.remove(e)
remove_dubs(L10,L11)
remove_dubs_new(L10,L11)
print(L10)

print('------------------------------------------------------------')
"""
     - is will return True if two variables point to the same object,
     - == if the objects referred to by the variables are equal.

     - == is for value equality. Use it when you would like to know if two objects have the same value.
     - is is for reference equality. Use it when you would like to know if two references refer to the same object.

     >>> 1000 is 10**3
         False
     >>> 1000 == 10**3
         True

     >>> a = [1, 2, 3]
     >>> b = a
     >>> b is a
         True
     >>> b == a
         True
     >>> b = a[:]
     >>> b is a
         False
     >>> b == a
         True
"""
aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
print(aList == bList)
print(aList is bList)


cList = [6, 5, 4, 3, 2]
dList = []

for num in cList:
    dList.append(num)

print(cList == dList)
print(cList is dList)
cList[2] = 20
print(cList)
print(dList)

print([] is [])
print([] == [])