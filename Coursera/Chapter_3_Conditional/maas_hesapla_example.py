rHour = raw_input("Enter Hours: ")
try:
    iHour = int(rHour)
except:
    iHour = -1
    print "Error , please enter numeric input"

rRate = raw_input("Enter Rate: ")
try:
    iRate = int(rRate)
except:
    iRate = -1
    print "Error , please enter numeric input"

if iRate != -1 & iHour != -1:
    if iHour > 40:
        extra_hour = iHour - 40
        salary = 40 * iRate + extra_hour * iRate * 1.5
        print salary
    else:
        print 40 * iRate
