
# class inheritance

class Person:

    # Initializer (constructor)
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return "{} {}".format(self.name, self.surname)


class Employee(Person):

    # static attribute
    department = 'IT'

    # static method
    @staticmethod
    def static_method(param):
        print(param)


####################
emp1 = Employee('Ion', 'Popescu')
emp2 = Employee('Geta', 'Ionescu')
print(emp1.department, emp2.department)

Employee.department = "Logistics"
print(emp1.department, emp2.department)

emp1.department = "Help Desk"
print(emp1.department, emp2.department)

Employee.static_method('Something static')
