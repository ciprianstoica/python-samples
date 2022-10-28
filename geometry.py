from math import pi


class WrongGeometry(Exception):
    pass


class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __add__(self, other):
        return Segment(self, other)

    def get_distance(self) -> float:
        return round((self.x ** 2 + self.y ** 2) ** 0.5, 2)

    def get_distance_to_other(self, p) -> float:
        return round(((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5, 2)


class Circle(Point):

    def __init__(self, x: float, y: float, r: float):
        super().__init__(x, y)
        self.r = r

    def __repr__(self):
        return f'Circle({self.x}, {self.y}, {self.r})'

    # def __str__(self):
    #     return f'Circle at coordinates ({self.x}, {self.y}) and radius {self.r}'

    # def __del__(self):
    #     print(f'Circle({self.x}, {self.y}, {self.r}) destroyed')

    def get_area(self):
        return round(pi * self.r ** 2, 4)

    def get_distance(self) -> float:
        return round(super().get_distance() - self.r, 2)


class Segment:

    def __init__(self, p1: Point, p2: Point):
        if type(p1) != Point:
            raise WrongGeometry(f"only Point objects allowed. '{type(p1).__name__}' given")
        if type(p2) != Point:
            raise WrongGeometry(f"only Point objects allowed. '{type(p2).__name__}' given")
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f'Segment({self.p1}, {self.p2})'
        # return f'Segment(Point({self.p1.x}, {self.p1.y}), Point({self.p2.x}, {self.p2.y}))'

    def __lt__(self, other):
        return self.get_length() < other.get_length()

    def __le__(self, other):
        return self.get_length() <= other.get_length()

    def __gt__(self, other):
        return self.get_length() > other.get_length()

    def __ge__(self, other):
        return self.get_length() >= other.get_length()

    def __eq__(self, other):
        return self.get_length() == other.get_length()

    def __ne__(self, other):
        return self.get_length() != other.get_length()

    def get_length(self) -> float:
        # return round(((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2) ** 0.5, 2)
        return self.p1.get_distance_to_other(self.p2)


class Rectangle:

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f'Rectangle({self.p1}, {self.p2})'

    def __eq__(self, other):
        return self.get_sides() == other.get_sides()

    def get_sides(self) -> list:
        return sorted([abs(self.p1.x - self.p2.x), abs(self.p1.y - self.p2.y)])

    def get_area(self) -> float:
        l1, l2 = self.get_sides()
        return l1 * l2

    def get_perimeter(self) -> float:
        l1, l2 = self.get_sides()
        return (l1 + l2) * 2

    def contains(self, p):
        lx = sorted([self.p1.x, self.p2.x])
        ly = sorted([self.p1.y, self.p2.y])

        if type(p) == Point:
            if lx[0] <= p.x <= lx[1] and ly[0] <= p.y <= ly[1]:
                return True
        elif type(p) == Circle:
            if lx[0] <= p.x - p.r and p.x + p.r <= lx[1] and \
                    ly[0] <= p.y - p.r and p.y + p.r <= ly[1]:
                return True
        return False


class Polyline:

    def __init__(self, p1: Point, p2: Point, *points: Point):
        self.points = [p1, p2, *points]
        for p in points:
            if type(p) != Point:
                raise WrongGeometry(f"only Point objects allowed. '{type(p).__name__}' given")

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.points):
            return self.points[self.index]
        raise StopIteration

    def __len__(self):
        return len(self.points)

    def __getitem__(self, item):
        if type(item) == int:
            return self.points[item]
        elif type(item) == slice:
            return Polyline(*self.points[item])
        else:
            raise WrongGeometry("only 'int' or 'slice' allowed")

    def __str__(self):
        r = 'Polyline('
        for p in self.points:
            r += f'{p}, '
        r = r.rstrip(', ') + ')'
        return r


if __name__ == '__main__':
    p1 = Point(3, 6)
    p2 = Point(6, 4)

    poly = Polyline(p1, p2, Point(-5, -6))

    for p in poly:
        print(p)

    for i in range(len(poly)):
        print(poly[i])

    print(poly)
    print(poly[::-1])



    # p3 = Point(3, 5)
    # c = Circle(14, 5, 1)
    # r = Rectangle(p1, p2)
    # print(r.contains(c))
    # print(r.get_sides())
    # print(r.get_area())
    # print(r.get_perimeter())
    # r1 = Rectangle(Point(3, 4), Point(6, 8))
    # r2 = Rectangle(Point(-6, -8), Point(-3, -4))
    # print(r1 == r2)

    # s = Segment(23, Point(3, 6))
    # print(s)





