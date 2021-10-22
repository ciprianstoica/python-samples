from abc import ABC, abstractmethod


class MyAbsClass(ABC):

    def __init__(self, p):
        self.p = p

    @abstractmethod
    def abs_method(self):
        self.p += 1

    def normal_method(self):
        return self.p * 2


class MyClass(MyAbsClass):

    def abs_method(self):
        super().abs_method()
        return self.p ** 2


o2 = MyClass(3)
print(o2.abs_method())

# ERROR
o1 = MyAbsClass(5)

