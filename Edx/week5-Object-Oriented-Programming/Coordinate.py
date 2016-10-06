# the word object means that Coordinate is a Python object and inherits all its attributes
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        if self is None or other is None:
            return False
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Coordinate({}, {})".format(self.x, self.y)

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5


c = Coordinate(3, 4)
origin = Coordinate(0, 0)
print(type(c))
print(c.__str__())
print(c.x)
print(origin.y)
print(c.distance(origin))
print(Coordinate.distance(c, origin))

# use isinstance() to check if an object is a Coordinate
print(isinstance(c, Coordinate))

'''
    like print, can override these to work with your class
    define them with double underscores before/after
    __add__(self, other) --> self + other
    __sub__(self, other) --> self -other
    __eq__(self, other) -->  self == other
    __lt__(self, other) -->  self < other
    __len__(self)        --> len(self)
    __str__(self)        --> print(self)
'''

originNew = Coordinate(origin.x, origin.y)
c = origin
print(origin is c)  # shows same reference
print(originNew is c)
print(eval(repr(c)))
