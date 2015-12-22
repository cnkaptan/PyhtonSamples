# A list element can be any phyton object even another list
# a list can be empty
print [1, 23, 76]
print ['red', 'yellow', 'blue']
print ['red', 24, 98.6]
print [1, [5, 6], 7]
print []

for i in [5, 4, 3, 2, 1]:
    print i
print "Blastoff!"

friends = ['Joseph', "Glenn", "Sally"]
print friends[1]
for friend in friends:
    print "Happy New Year:", friend
print "Done"

greet = "Hello Bob"
print len(greet)
x = [1, 2, "Joe", 99]
print len(x)

# the range function returnns a list of numbers that
# range from zero to one less than the paramater

print range(4)
print len(friends)
print range(len(friends))

for i in range(len(friends)):
    friend = friends[i]
    print "Happy New Year:", friend
