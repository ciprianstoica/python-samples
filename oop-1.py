
# class Person(object): # old Python 2.x notation
class Person:

    # Initializer (constructor)
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return "{} {}".format(self.name, self.surname)


person = Person('Ion', 'Popescu')

print(person.get_fullname())
