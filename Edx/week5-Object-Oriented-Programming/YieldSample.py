def genTest():
    yield 1
    yield 2
    3
    yield 4


foo = genTest()

print(foo.__next__())
print(foo.__next__())
print(foo.__next__())
# print(foo.__next__()) # Results in a StopIterationexception

for n in genTest():
    print(n)

print(type(genTest()))


def genFib():
    fibn_1 = 1  # fib(n-1)
    fibn_2 = 0  # fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

fib = genFib()
