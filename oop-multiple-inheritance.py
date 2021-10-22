
# multiple inheritance

class A:

    def __init__(self):
        self.name = 'name A'

    def specific_a(self):
        print("This is specific to class A")

    def generic(self):
        print("AAAA")


class B:

    def __init__(self):
        self.name = 'name B'

    def specific_b(self):
        print("This is specific to class B")

    def generic(self):
        print("BBBB")


class C(A, B):
    pass
    # def generic(self):
    #     B.generic(self)

    def getg(self):
        return super(A, self).name


c = C()
c.generic()
print(c.getg())