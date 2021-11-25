
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        if type(other) == Polyline:
            return Polyline(self, *other.points)
        elif type(other) == Point:
            return Polyline(self, other)

    def __radd__(self, other):
        if type(other) == Polyline:
            return Polyline(*other.points, self)
        elif type(other) == Point:
            return Polyline(other, self)

    def get_distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Polyline:
    """A polyline is a list of points"""

    def __init__(self, *args):
        for p in args:
            if type(p) != Point:
                raise TypeError(f'Only Point objects allowed, {type(p)} received')
        self.points = list(args)

    def __str__(self):
        s = 'Polyline('
        for p in self.points:
            s += f'{p}, '
        return s.strip(', ') + ')'

    def __gt__(self, other):
        return self.get_length() > other.get_length()

    def __ge__(self, other):
        return self.get_length() >= other.get_length()

    def __lt__(self, other):
        return self.get_length() < other.get_length()

    def __le__(self, other):
        return self.get_length() <= other.get_length()

    def __eq__(self, other):
        return self.get_length() == other.get_length()

    def __ne__(self, other):
        return self.get_length() != other.get_length()

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.points):
            del self.index
            raise StopIteration
        return self.points[self.index]

    def __len__(self):
        return len(self.points)

    def __getitem__(self, item):
        return self.points[item]

    def __add__(self, other):
        return Polyline(*self.points, other)

    def get_length(self):
        l = len(self.points)
        if l < 2:
            return 0
        length = 0
        for i in range(l - 1):
            length += self.points[i].get_distance(self.points[i + 1])
        return length


if __name__ == '__main__':

    poly1 = Polyline(Point(3, 4), Point(5, 9), Point(2, 7))
    poly2 = Polyline(Point(-3, 14), Point(32, 4), Point(12, 8), Point(5, 8))

    # test __str__
    print(poly1)

    # class is iterable
    for p in poly2:
        print(p)

    # class is subscriptable
    for i in range(len(poly2)):
        print(poly2[i])

    # comparison operators are overloaded
    print(poly1 < poly2)
    print(poly1 >= poly2)

    # add operator is overloaded
    poly = Point(3, 4) + Point(5, 9) + Point(2, 7)
    print(poly)
