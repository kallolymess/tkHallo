import datetime

# dunder methods https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types

# It helps to look at https://github.com/python/cpython/blob/master/Lib/datetime.py
# where you can find how python handles the __add__ __str__ and class date
# included the datetime.py to the repo

class Employee:
 
    raise_ammount = 1.02

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_ammount)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

# this time we will look at dunder add. 
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())    

emp1 = Employee('Robertsonn', 'Jabberwalkie', 40000)
emp2 = Employee('Truely', 'Duely', 50000)
emp3 = Employee('Susan', 'Smith', 60000)

print(emp1 + emp2)
# or
print(emp1.__add__(emp3))

print(len(emp1))


