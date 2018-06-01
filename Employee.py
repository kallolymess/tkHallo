import datetime

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

# Dunders are methods surrounded by "__". 
# __repr__ is an unambiguous representation of an object and should be used for debugging and logging purposes
# __str__ is a printable representation of the object usually meant for end users.

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)        

emp1 = Employee('Robertsonn', 'Jabberwalkie', 40000)
emp2 = Employee('Truely', 'Duely', 50000)
emp3 = Employee('Susan', 'Smith', 60000)

# print(emp1) will try to find the __str__ first for that object
# if that is not found it will try to fall back to __repr__.
print(emp1)    

# it is however always possible to print out the __str__ and __repr__ explicitly if needed
print(repr(emp2))
print(str(emp3))
# or we can do
print(emp1.__repr__())
print(emp1.__str__())
