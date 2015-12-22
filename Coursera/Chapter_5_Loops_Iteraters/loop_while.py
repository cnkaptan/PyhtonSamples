n = 5

while n > 0:
    print n
    n -= 1
print "Blastoff!"
print n

while True:
    line = raw_input("> ")
    if line == "Done":
        break
    print line
print "done!"
