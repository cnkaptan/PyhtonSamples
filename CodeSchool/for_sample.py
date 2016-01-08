from math import *
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index+1, item

for item in choices:
    print item


list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    if a > b:
        print a
    else:
        print b

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
#for un elsi normal bir sekilde biterse calisir
print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'


def is_int(x):
    if type(x) == int and x == round(x,1):
        return True
    return False

print is_int(7.0)