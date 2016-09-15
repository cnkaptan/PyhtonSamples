nameHandle = open('kids', 'w')

for i in range(2):
    name = input('Enter a name: ')
    nameHandle.write(name + '\n')
nameHandle.close()

nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line, end='')

nameHandle.close()
