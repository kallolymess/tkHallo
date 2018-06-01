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

# We can see that just this will fully create a subclass
class Developer(Employee):
    pass

# Test Subclassing
emp1 = Developer('Kallol', 'Biswas', 40000)
emp2 = Developer('Corey', 'Schafer', 50000)
emp3 = Employee('Dave', 'Dey', 60000)

print(emp1.fullname())
print(emp2.fullname())
print(emp3.fullname())

#here is a Pretty handy Python function help()
print(help(Developer))
"""
Help on class Developer in module __main__:

class Developer(Employee)
 |  # We can see that just this will fully create a subclass
 |
 |  Method resolution order:
 |      Developer
 |      Employee
 |      builtins.object
 |
 |  Methods inherited from Employee:
 |
 |  __init__(self, first, last, pay)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  apply_raise(self)
 |
 |  fullname(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Employee:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Employee:
 |
 |  raise_ammount = 1.02
"""
