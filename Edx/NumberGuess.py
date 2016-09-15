low = 0
high = 100
ans = int((low + high) / 2)
flag = ''
print("Please think of a number between 0 and 100!")

while flag != 'c':
    print('Is your secret number %s?' % ans)

    flag = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.Enter 'c' to indicate I guessed correctly.")
    if flag == 'h':
        high = ans
    elif flag == 'l':
        low = ans
    elif flag == 'c':
        print("Game over. Your secret number was: %d" % ans)
        break
    else:
        print('Sorry, I did not understand your input.')
        continue
    ans = int((low + high) / 2)
