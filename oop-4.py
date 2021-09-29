
# polymorphism

class Person:

    # Initializer (constructor)
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return "{} {}".format(self.name, self.surname)


class Employee(Person):

    department = "IT"

    def get_fullname(self):
        return "{} {}".format(self.name.upper(), self.surname.upper())


person_list = [
    Employee('Geta', 'Popescu'),
    Person('Gicu', 'Ionescu'),
    Employee('Maria', 'Toader')
    ]

for person in person_list:
    print(person.get_fullname())
