
# suggests that the params should be str respectively int and the result should be str
def func(s: str, i: int) -> str:
    return s * i


# suggest that the param should be either int or str and the result either int or str
def func2(a: int or str) -> int or str:
    return a * 2


# Python 2.7 hinting style
def func3(a):
    # type: (int or float) -> int or float
    return a ** 2


a: int = 6

a = 'abc'

#print(a)
#print(func(5, 'Ab'))

# check hints
d = func(22, 'a') * 'ab'


