try:
    rawPoint = raw_input("Enter Your Point")
    fPoint = float(rawPoint)

    if fPoint >= 0.0 & fPoint <= 1.0:
        if fPoint >= 0.9:
            print "A"
        elif fPoint >= 0.8:
            print "B"
        elif fPoint >= 0.7:
            print "C"
        elif fPoint >= 0.6:
            print "D"
        else:
            print "F"
    else:
        print "Error, Out of Range\nEnter point between 0.0 and 1.0"
except:
    print "Enter Numerical Point"