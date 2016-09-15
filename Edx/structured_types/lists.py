"""
    ordered sequence of information, accessable by index
    a list is denoted by square brackets , []
    a list containes elements:
            usually homogeneous (i.e .. all integers)
            can contain mix types( not common )

    list elements can be changed so a list is mutable

"""

a_list = []
print(type(a_list))
b_list = [2, 'a', 4, True]
L = [2, 1, 3]

print(len(L))

print(L[0])

print(L[2] + 1)

print(L[1])
L[1] = 5  # yeni liste yaratmaz , L nin elemanini degistirir
print(L)

for element in L:
    print(element, end=" ")
print()
for i in range(len(L)):
    print(L[i], end=" ")

x = [1, 2, [3, 'John', 4], 'Hi']

print(x[0])
print(x[2])
print(type(x[2]))
print(x[-1])
print(x[2][2])
print(x[2][1][2])
print(x[0:1]) # [1] liste doner
print(type(x[0:1]))
print(x[0])
print(type(x[0])) # elemani doner
print(2 in x)
print(3 in x)
x[0] = 8
print(x)
