import time
# unefficent fibonacci

def fib(n):
    global numFibCalls # accessible from outside scope of function
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)



def fib_efficent(n, d):
    global numFibCalls # accessible from outside scope of function
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficent(n - 1, d) + fib_efficent(n - 2, d)
        d[n] = ans
        return ans

numFibCalls = 0
millis = int(round(time.time() * 1000))
print(fib_efficent(30, {1: 1, 2: 2}),numFibCalls)
print(int(round(time.time() * 1000))-millis)

numFibCalls = 0
millis = int(round(time.time() * 1000))
print(fib(30),numFibCalls)
print(int(round(time.time() * 1000))-millis)
