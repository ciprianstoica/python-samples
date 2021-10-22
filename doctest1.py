
# define a function to test
def factorial(n):
    """
    Calculates factorial
    Define input and expected output:
    >>> factorial(5)
    120
    >>> factorial(7)
    50401
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    from doctest import testmod
    # testmod()
    testmod(name='factorial', verbose=True)
    testmod(name='factorial2')