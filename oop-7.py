class Punct:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Punct({self.x}, {self.y})'

    def __add__(self, other):
        if type(other) == Punct:
            return Polilinie(self, other)
        elif type(other) == Polilinie:
            l = [self]
            for punct in other.puncte:
                l.append(punct)
            return Polilinie(*l)

    def get_dist(self, p):
        d = ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5
        if type(p) == Punct:
            return d
        elif type(p) == Cerc:
            return d - p.r

class Cerc(Punct):

    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def get_dist(self, p):
        return super().get_dist(p) - self.r

class Segment:

    def __init__(self, p1: Punct, p2: Punct):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        # f'Segment(Punct{self.p1.x}, {self.p2.y}), Punct({self.p2.x}, {self.p2.y}))'
        return f'Segment({self.p1}, {self.p2})'

    def __gt__(self, other):
        print('__gt__ caled...')
        if self.get_length() > other.get_length():
            return True
        else:
            return False


    def get_length(self):
        """Gets the length of the segment"""
        return self.p1.get_dist(self.p2)

class Polilinie:

    # def __init__(self, l: list):
    #     self.l = l

    def __init__(self, *args):
        self.puncte = list(args)

    def __str__(self):
        s = 'Polilinie('
        for p in self.puncte:
            s += str(p) + ', '
        s = s.rstrip(', ')
        s += ')'
        return s

    def __add__(self, other):
        if type(other) == Punct:
            poli = Polilinie(*self.puncte)
            poli.puncte.append(other)
            return poli
        elif type(other) == Polilinie:
            l = self.puncte + other.puncte
            return Polilinie(*l)

    def __iter__(self):
        self.current = 0
        #print('##### Executed __iter__')
        return self

    def __next__(self):
        #print('##### Executed __next__')
        if self.current >= len(self.puncte):
            del self.current
            raise StopIteration
        else:
            self.current += 1
            return self.puncte[self.current - 1]

    def __getitem__(self, item):
        return self.puncte[item]

    def __len__(self):
        return len(self.puncte)

p1 = Punct(1, 1)
p2 = Punct(2, 2)

#poly1 = Polilinie(p1, p2)
#print(poly1)
poly2 = Punct(0,0) + p1 + (p2 + Punct(3, 3))
print(poly2)

for punct in poly2:
    print(punct)

for i in range(0, len(poly2)):
    print(poly2[i])


# s = p1 + p2
# s = Segment(p1, p2)
# print(s)

#
# s1 = Segment(Punct(1,1), Punct(2,2))
# s2 = Segment(Punct(-11,-11), Punct(20,20))
#
# if s1 >= s2:
#     print('s2 este mai mare')
# else:
#     print('s1 este mai mare')



