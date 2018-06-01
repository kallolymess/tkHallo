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
    raise_ammount = 1.1

# Creating the constructor for the Subclass, and passing the 
# class variables to the super class, in this case to class Employee 
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
# This is equivalent to Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

# Test Subclassing
emp1 = Developer('Kallol', 'Biswas', 40000, 'python')
emp2 = Developer('Corey', 'Schafer', 50000, 'Java')
emp3 = Employee('Dave', 'Dey', 60000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.fullname())
print(emp1.pay)

print(emp1.__dict__)