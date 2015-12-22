numList = list()

while True:
    inp = raw_input("Enter a number: ")
    if inp == 'done':
        break
    value = float(inp)
    numList.append(value)

average = sum(numList) / len(numList)
print "Average:", average
