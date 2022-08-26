class WrongGeometry(Exception):
    pass


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __del__(self):
        pass
        # print('S-a distrus obiectul', self)

    def __add__(self, other):
        return Segment(self, other)

    def get_distance(self):
        return round((self.x ** 2 + self.y ** 2) ** 0.5, 2)


class Circle(Point):

    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def __repr__(self):
        return f'Circle({self.x}, {self.y}, {self.r})'

    def get_distance(self):
        return round(super().get_distance() - self.r, 2)


class Segment:

    def __init__(self, p1: Point, p2: Point):
        if type(p1) != Point:
            raise WrongGeometry(f"Incorrect type. Only Point allowed. '{type(p1).__name__}' given.")
        if type(p2) != Point:
            raise WrongGeometry(f"Incorrect type. Only Point allowed. '{type(p2).__name__}' given.")
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        # return f'Segment(Point({self.p1.x}, {self.p1.y}), Point({self.p2.x}, {self.p2.y}))'
        return f'Segment({self.p1}, {self.p2})'

    def __gt__(self, other):
        return self.get_length() > other.get_length()

    def __ge__(self, other):
        return self.get_length() >= other.get_length()

    def __lt__(self, other):
        return self.get_length() < other.get_length()

    def __le__(self, other):
        return self.get_length() <= other.get_length()

    def get_length(self):
        return round((
            (self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2) ** 0.5, 2)


class Polyline:

    def __init__(self, p1: Point, p2: Point, *points: Point):
        self.__index = -1
        self.points = [p1, p2, *points]
        for p in self.points:
            if type(p) != Point:
                raise WrongGeometry(f"Incorrect type. Only Point allowed. '{type(p1).__name__}' given.")

    def __repr__(self):
        r = 'Polyline('
        for p in self.points:
            r += f'{p}, '
        return r.rstrip(', ') + ')'

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        self.__index += 1
        if self.__index == len(self.points):
            raise StopIteration
        return self.points[self.__index - 1]

    def __len__(self):
        return len(self.points)

    def __getitem__(self, item):
        return self.points[item]


class Rectangle:

    def __init__(self, p1: Point, p2: Point):
        if type(p1) != Point:
            raise WrongGeometry(f"Incorrect type. Only Point allowed. '{type(p1).__name__}' given.")
        if type(p2) != Point:
            raise WrongGeometry(f"Incorrect type. Only Point allowed. '{type(p2).__name__}' given.")
        self.p1 = p1
        self.p2 = p2

    def get_dimensions(self):
        """
        Returns a list with the dimensions.

        Returns:
            list: the list with the dimensions

        >>> r = Rectangle(Point(2, 3), Point(4, 6))
        >>> r.get_dimensions()
        [2, 3]
        """

        return [abs(self.p1.x - self.p2.x), abs(self.p1.y - self.p2.y)]

    def get_area(self):
        lat1, lat2 = self.get_dimensions()
        return lat1 * lat2

    def get_perimeter(self):
        """
        Gets the perimeter of the rectangle.

        Returns:
            float: the perimeter

        >>> r = Rectangle(Point(2, 3), Point(4, 6))
        >>> r.get_perimeter()
        10
        """
        lat1, lat2 = self.get_dimensions()
        return round((lat1 + lat2) * 2, 2)


if __name__ == '__main__':
    from doctest import testmod
    testmod()

    poly = Polyline(Point(2, 3), Point(3, 4), Point(4, 5))

    for p in poly:
        print(p)

    for i in range(len(poly)):
        print(poly[i])






