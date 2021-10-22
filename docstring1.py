# NumPy/SciPy docstring example

import random


class Person:
    """This is summary of the description of the class

    This is a longer description of the purpose of the class.
    Use as many lines as necessary here.

    Attributes
    ----------
    name : str
        the name of the person
    surname : str
        the surname of the person
    id : int
        randomly generated id

    Methods
    -------
    get_fullname()
        Prints the person fullname.
    """

    def __init__(self, name, surname):
        """This is the constructor

        Parameters
        ----------
        name : str
            the name of the person
        surname : str
            the surname of the person

        Raises
        ------
        TypeError
            If name or surname are not strings
        """
        if type(name) != str or type(surname) != str:
            raise TypeError('Only strings allowed')
        self.name = name
        self.surname = surname
        self.id = random.randint(0, 100)

    def get_fullname(self):
        """Gets the full name of the person

        Returns
        -------
        str
            the full name of the person
        """

        return f"{self.name} {self.surname}"


p = Person('Ion', 'Pop')
help(Person)
p.get_fullname() + 456

