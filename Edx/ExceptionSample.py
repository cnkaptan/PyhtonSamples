a = "Cihan"
print(a[:-1])
try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me one number:"))
    print(a / b)
    print("Okay")
except ValueError:
    print("Could not convert to a number")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Something went very wrong")
print("Outside")

data = []
file_name = input("Provide a name of file of data")

try:
    fh = open(file_name, 'r')
except IOError:
    print('can not open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')
            data.append(addIt)
finally:
    fh.close()  # close file even if fail



