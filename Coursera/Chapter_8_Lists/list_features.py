a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print a
print b
print c
print "\n"
t = [9, 41, 12, 3, 74, 15]
print t[1:3]
print t[:4]
print t[3:]
print t[:]
print t
print "\n"
x = list()
print type(x)
print dir(x)

# We can create an empty list and then add elements using the append method
# The list stays in order and new elements are added at the end of the list
print "\n"
stuff = list()
stuff.append("book")
stuff.append(99)
print stuff
stuff.append('cookie')
print stuff

print "\n"
some = [1, 9, 21, 10, 16]
print 9 in some
print 15 in some
print 20 not in some

print "\n"
numbers = [3, 1, 6, 2, 9, 8]
numbers.sort()
print numbers
friends = ["Joseph", 'Glenn', "Sally"]
friends.sort()
print friends
print friends[1]

print "\n"
# These are a number of functions built into Python that take lists as parameters
nums = [3, 41, 12, 9, 74, 15]
print len(nums)
print max(nums)
print min(nums)
print sum(nums)
print sum(nums)/len(nums)
