
x = float(input('Enter a decimal number between 0 and 1: '))

p = 0

while ((2**p)*x)%1 !=0:
    print("Remainder = " + str((2**p)*x-int((2**p)*x)))
    p+=1

num = int(x*(2**p))

print(num)

result = ''
if num == 0:
    result = '0'

while num > 0:
    result = str(num % 2) + result
    num //= 2

for i in range(p - len(result)):
    result = '0' + result

print(result)
result = result[0:-p] + '.' + result[-p:]

print(result)