class WrongGeometry(Exception):
    pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return f'Punctul de coordonate({self.x}, {self.y})'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    # def __del__(self):
    #     print(f'distrus Point({self.x}, {self.y})')

    def get_distance(self):
        return round((self.x ** 2 + self.y ** 2) ** 0.5, 2)


class Circle(Point):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def __repr__(self):
        return f'Circle({self.x}, {self.y}, {self.r})'

    def get_distance(self):
        return super().get_distance() - self.r


class Segment:

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

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

    def get_length(self):
        return round(((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2) ** 0.5, 2)


class Rectangle:

    def __init__(self, p1: Point, p2: Point):
        # if not isinstance(p1, Point) or not isinstance(p2, Point):
        if type(p1) != Point:
            raise WrongGeometry(f'Expected Point, got {type(p1).__name__}')
        if type(p2) != Point:
            raise WrongGeometry(f'Expected Point, got {type(p2).__name__}')
        self.p1 = p1
        self.p2 = p2
        self.sides = [abs(self.p1.x - self.p2.x), abs(self.p1.y - self.p2.y)]

    def __str__(self):
        return f'Rectangle({self.p1}, {self.p2})'
        # return f'Rectangle(Point({self.p1.x}, {self.p1.y}), Point({self.p2.x}, {self.p2.y}))'

    def get_sides(self) -> list:
        return self.sides

    def get_area(self) -> float or int:
        return self.sides[0] * self.sides[1]

    def get_perimeter(self) -> float or int:
        return (self.sides[0] + self.sides[1]) * 2

    def contains(self, c: Circle):
        return (self.p1.x <= c.x + c.r <= self.p2.x or self.p2.x <= c.x + c.r <= self.p1.x or
                self.p1.x <= c.x - c.r <= self.p2.x or self.p2.x <= c.x - c.r <= self.p1.x) and \
               (self.p1.y <= c.y + c.r <= self.p2.y or self.p2.y <= c.y + c.r <= self.p1.y or
                self.p1.y <= c.y - c.r <= self.p2.y or self.p2.y <= c.y - c.r <= self.p1.y)


class Polyline:

    def __init__(self, p1: Point, p2: Point, *points: Point):
        self.points = (p1, p2, *points)
        for p in self.points:
            if type(p) != Point:
                raise WrongGeometry(f'Expected Point, got {type(p).__name__}')

    # def __init__(self, *points: Point):
    #     if len(points) < 2:
    #         raise WrongGeometry('Minimum 2 points are mandatory')
    #     for p in points:
    #         if type(p) != Point:
    #             raise WrongGeometry(f'Expected Point, got {type(p).__name__}')
    #     self.points = points

    def __repr__(self):
        ret = 'Polyline('
        for p in self.points:
            ret += f'{p}, '
        ret = ret.rstrip(', ') + ')'
        return ret


if __name__ == '__main__':
    # re = Rectangle(Point(3, 4), Point(-2, -6))
    # re2 = Rectangle(Point(2, 3), Circle(2, 3, 5))
    # print(re2)
    # print(re.get_sides())
    # print(re.get_area())
    # print(re.get_perimeter())
    # print(re)
    #
    # print(re.contains(Circle(1, -1, 2)))

    poli = Polyline(Point(2, 3), Point(4, 3), Point(2, 9), Point(-5, 0))
    print(poli)

