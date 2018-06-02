import datetime

# its about Property Decorators - Getters, Setters and Deleters

class Employee:
 
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Robertsonn', 'Jabberwalkie', 40000)

print(emp1.first)
print(emp1.email)
print(emp1.fullname())
