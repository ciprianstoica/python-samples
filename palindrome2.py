
def palindrom(p, case_sensitive=True):
    """Tells if param is palindrome

        Parameters
        ----------
        p : str or int or list
            input parameter
        case_sensitive : bool
            case sensitive or not

        Raises
        ------
        TypeError
            if type is not str, int or list

        >>> palindrom(['ABC', 12, True, 12, 'abc'])
        False

        >>> palindrom(['ABC', 12, True, 12, 'abc'], case_sensitive=False)
        True

        >>> palindrom('Cojoc')
        False

        >>> palindrom('Cojoc', case_sensitive=False)
        True

        >>> palindrom(12345)
        False

        >>> palindrom(1234554321)
        False
    """

    if type(p) is int:
        p = str(p)
    elif type(p) is str:
        if case_sensitive is False:
            p = p.lower()
    elif type(p) is list:
        p = list(p)
        if case_sensitive is False:
            for i in range(len(p)):
                if type(p[i]) is str:
                    p[i] = p[i].lower()
    else:
        raise TypeError('Only int, str, list allowed')
    return p[::-1] == p


if __name__ == '__main__':
    from doctest import testmod
    testmod()

    # print(palindrom('Cojoc'))
    # print(palindrom('Cojoc', case_sensitive=False))
    # print(palindrom(12345))
    # print(palindrom(1234554321))

