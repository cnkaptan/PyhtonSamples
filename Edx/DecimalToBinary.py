num = -3
isNeg = False

if num < 0:
    num = abs(num)
    isNeg = True
else:
    isNeg = False

result = ''
if num == 0:
    result = '0'

while num > 0:
    result = str(num % 2) + result
    num //= 2

if isNeg:
    result = '-' + result

print(result)
