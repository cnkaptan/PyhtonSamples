class Fraction():
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)

    def getNumer(self):
        return self.numer

    def getDenom(self):
        return self.denom

    def __add__(self, other):
        numerNew = self.getNumer() * other.getDenom() + other.getNumer() * self.getDenom()
        denomNew = self.getDenom() * other.getDenom()
        return Fraction(numerNew, denomNew)

    def __sub__(self, other):
        numerNew = self.getNumer() * other.getDenom() - other.getNumer() * self.getDenom()
        denomNew = self.getDenom() * other.getDenom()
        return Fraction(numerNew, denomNew)

    def convert(self):
        return self.getNumer() / self.getDenom()

oneHalf = Fraction(1, 2)
twoThirds = Fraction(2, 3)
print(oneHalf)
print(twoThirds)

print(oneHalf.getNumer())
print(Fraction.getDenom(twoThirds))

new = oneHalf + twoThirds
print(new)
print(new.convert())



