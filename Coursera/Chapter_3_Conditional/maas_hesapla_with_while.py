iHour = -1
iRate = -1

while iRate == -1 & iHour == -1:
    try:
        rHour = raw_input("Enter Hours: ")
        iHour = float(rHour)
        rRate = raw_input("Enter Rate: ")
        iRate = float(rRate)
    except:
        rRate =-1
        iRate = -1
        print "Error , please enter numeric input"
        continue


if iHour > 40:
    extra_hour = iHour - 40
    salary = 40 * iRate + extra_hour * iRate * 1.5
    print salary
else:
    print 40 * iRate
