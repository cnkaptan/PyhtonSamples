import math


def polysum(n, s):
    def calculateArea(n, s):
        return (0.25 * n * s * s) / (math.tan(math.pi / n))

    def calculatePerimeter(n, s):
        return (n * s)**2

    return round(calculateArea(n, s),4) + calculatePerimeter(n, s)
