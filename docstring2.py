# reStructured Text doctring
# alternatives: Epytext, Google

def func(x, y=1):
    """Some description

    :param x: first parameter
    :type x: str

    :param y: second parameter (default is 1)
    :type y: int

    :returns: some return
    :rtype: str
    """

    return x * y


func(78, 3) + 678


def func2(x: object, y: object = 7) -> object:
    return x ** y
