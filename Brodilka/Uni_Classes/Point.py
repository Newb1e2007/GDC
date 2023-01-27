class Point:
    def __init__(self, x=0, y=0):
        assert (isinstance(x, (int, float, tuple, list, Point)))
        assert (isinstance(y, (int, float)))
        if isinstance(x, (tuple, list)):
            self.x = x[0]
            self.y = x[1]
        elif isinstance(x, Point):
            self.x = x.x
            self.y = x.y
        else:
            self.x = x
            self.y = y

    def __add__(self, other):
        assert(isinstance(other, Point))
        return Point(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        assert (isinstance(other, Point))
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        assert (isinstance(other, Point))
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        assert(isinstance(other, Point))
        return Point(self.x - other.x, self.y - other.y)

    def __rsub__(self, other):
        assert (isinstance(other, Point))
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        assert (isinstance(other, Point))
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        assert (isinstance(other, (int, float)))
        return Point(self.x * other, self.y * other)

    def __rmul__(self, other):
        assert (isinstance(other, (int, float)))
        return Point(self.x * other, self.y * other)

    def __imul__(self, other):
        assert (isinstance(other, (int, float)))
        return Point(self.x * other, self.y * other)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __eq__(self, other):
        assert (isinstance(other, Point))
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __int__(self):
        return int(self.length())

    def __float__(self):
        return self.length()

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __iter__(self):
        yield self.x
        yield self.y

    def length(self):
        return (self.x * self.x + self.y * self.y)**0.5
