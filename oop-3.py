
# overriding methods from BaseClass

class Person:

    # Initializer (constructor)
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return "{} {}".format(self.name, self.surname)


class Employee(Person):

    def __init__(self, name, surname, department):
        Person.__init__(self, name, surname)
        self.department = department

    def get_full_data(self):
        return "{} - {}".format(self.get_fullname(), self.department)


emp = Employee('Geta', 'Popescu', 'Human Resources')
print(emp.get_full_data())