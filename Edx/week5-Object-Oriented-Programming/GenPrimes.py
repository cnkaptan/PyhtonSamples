class GenPrimes():
    def __init__(self, stop):
        self.stop = stop


    def calculatePrimes(self):
        for i in range(3, self.stop+1, 1):
            flag = True
            for prime in self.earlierPrimes:
                if i % prime == 0:
                    flag = False
                    break
            if flag:
                self.earlierPrimes.append(i)
                yield i


# genPrime = GenPrimes(13)
# for i in genPrime.calculatePrimes():
#     print(i)


def genPrimes(x):
    earlierPrimes = [2, ]
    for i in range(3, x + 1, 1):
        flag = True
        for prime in earlierPrimes:
            if i % prime == 0:
                flag = False
                break
        if flag:
            earlierPrimes.append(i)
            yield i

for i in genPrimes(13):
    print(i)