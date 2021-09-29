

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def dist_to_origin(self):
        #return (self.x**2 + self.y**2)**0.5
        return self.dist_to_another_point(Point())

    def dist_to_another_point(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5


    def __add__(self, other):
        return Segment(self, other)


class Circle(Point):
    def __init__(self, x, y, radius):
        Point.__init__(self, x, y)
        self.radius = abs(radius)


    def __str__(self):
        return "Circle(Point({}, {}), radius = {})".format(self.x, self.y, self.radius)

    def __add__(self, other):
        if type(other).__name__ == 'tuple' and len(other) == 2:
            return Circle(self.x + other[0], self.y + other[1], self.radius)
        else:
            raise Exception("Tuple of 2 elements needed. {} given".format(len(other)))


    def dist_to_origin(self):
        return (Point.dist_to_origin(self) - self.radius)

    # def dist_to_another_point(self, p):
    #     return abs(Point.dist_to_another_point(self, p) - self.radius)
    #
    # def dist_to_another_circle(self, c):
    #     return abs(self.dist_to_another_point(c) - c.radius)

    def dist_to_another(self, a):
        if type(a).__name__ == 'Point':
            return abs(Point.dist_to_another_point(self, a) - self.radius)
        elif type(a).__name__ == 'Circle':
            if self.radius + a.radius >= Point.dist_to_another_point(self, a):
                return 0
            else:
                return abs(Point.dist_to_another_point(self, a) - self.radius - a.radius)


class Segment():
    def __init__(self, p1, p2):
        self.points = [p1, p2]


    def __lt__(self, other):
        return self.get_length() < other.get_length()


    def __gt__(self, other):
        return self.get_length() > other.get_length()


    def __eq__(self, other):
        return self.get_length() == other.get_length()


    def __str__(self):
        return "Segment(Point({}, {}), Point({}, {}))"\
            .format(self.points[0].x, self.points[0].y,
                    self.points[1].x, self.points[1].y)


    def get_length(self):
        return (self.points[0].dist_to_another_point(self.points[1]))




s1 = Segment(Point(0, 2), Point(0, 6))
s2 = Segment(Point(1, 6), Point(1, 10))


if s1 > s2:
    print("s1 > s2")
elif s1 < s2:
    print("s1 < s2")
elif s1 == s2:
    print("s1 == s2")

s = Point(0, 2) + Point(-4, 9)
print(s)



# p = Point(3, 4)
# c1 = Circle(55, 6, 7)
# c2 = Circle(-2, 1, 4)
#
#
#
# print(c2)
# c2.move((4,-7))
# print(c2)

# c3 = c2 + (4, -7)
# print(c2)
# print(c3)

# print(c1.dist_to_another(p))
# print(c1.dist_to_another(c2))
# print(c2.dist_to_another(c1))
# print(c2.dist_to_another(c2))

#print(c1)
#ppoint = POINT(0,0)

#print("{0:.4f}".format(point.dist_to_another_point(Point(2,3))))

#print(ppoint.dist_to_another_point(ppoint))

#print(point.dist_to_origin())

#circle = CIRCLE(3,4,6)

#print(circle.dist_to_origin())
