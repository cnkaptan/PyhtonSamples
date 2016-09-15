cube = 8
epsilon = 0.001
guess = 0.0
increment = 0.001
num_guess = 0

while guess <= cube:
    if abs(guess ** 3 - cube) < epsilon:
        break
    else:
        guess += increment

    guess += increment
    num_guess += 1
print('num_guesses =', num_guess)
if abs(guess ** 3 - guess) < epsilon:
    print('failed on cube root of', cube)
else:
    print('%.4f is close to the cube root of %d' % (guess, cube))

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0
num_guess = 0
while guess <= x:
    num_guess += 1
    if abs(guess ** 2 - x) < epsilon:
        break
    else:
        guess += step
print('num_guesses =', num_guess)
if abs(guess ** 2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

x = 25
epsilon = 0.01
num_guess = 0
low = 1.0
high = x
ans = (high + low) / 2

while abs(ans ** 2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' answer = ' + str(ans))
    num_guess += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (low + high) / 2

print('numGuess = ' + str(num_guess))
print(str(ans) + ' is close to square root of ' + str(guess))