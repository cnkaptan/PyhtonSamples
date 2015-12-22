abc = "With three words"
stuff = abc.split()
print stuff
print len(stuff)
print stuff[0]
print "\n"
for w in stuff:
    print w

print "\n"
line = "A lot                     of spaces"
etc = line.split()
print etc

print "\n"
line = "first;second;third"
thing = line.split()
print thing
print len(thing)
print "\n"
thing = line.split(';')
print thing
print len(thing)
