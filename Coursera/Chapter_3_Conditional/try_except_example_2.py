rawstr = raw_input("Bir Sayi Girin: ")

try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print "Nice Work"
else:
    print "Not a Number"
