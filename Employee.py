import datetime

class Employee():
 
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

emp1 = Employee('Kallol', 'Biswas', 40000)
emp2 = Employee('Corey', 'Schafer', 50000)
emp3 = Employee('Dave', 'Dey', 60000)

print(emp1.fullname())