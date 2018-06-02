import datetime

# dunder methods https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types

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

emp1 = Employee('Robertsonn', 'Jabberwalkie', 40000)
emp2 = Employee('Truely', 'Duely', 50000)
emp3 = Employee('Susan', 'Smith', 60000)

print(emp1 + emp2)
# or
print(emp1.__add__(emp3)) 

# here is how we use it
# print(1+2)
# print('a'+'b')
# this is where it comes from 
# print(int.__add__(1,2))
# print(str.__add__('a','b'))
