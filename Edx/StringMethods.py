str1 = 'exterminate!'
str2 = 'number one - the larch'

print(str1.upper)
print(str1.upper())
print(str1.upper().isupper())

print(str1.islower())

str3 = str2.capitalize()

print(str3)

print(str2.swapcase())

print(str1.index('e'))

print(str2.index('o'))  # ValueError verir

print(str2.find('n'))  # bulamayinca -1 doner

# print(str2.index('!'))

print(str2.find('!'))

print(str1.count('e'))

str4 = str1.replace('e', '*')

print(str4)

str5 = str2.replace('one', 'seven')

print(str2)

print(str5)
