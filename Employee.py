import datetime

# its about Property Decorators - Getters, Setters and Deleters

class Employee:
 
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
# We are going to change the email from being a Class Variable to 
# a Method and then add the property Decorator @property 
# so that python handles it as a VARIABLE. 
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Robertsonn', 'Jabberwalkie', 40000)

emp1.first = 'Kalipso'

print(emp1.first)
# if email would have been left as normal Variable (self.email = first + '.' + last + '@company.com') 
# it would show Robertsonn.Jabberwalkie@company.com instead of Kalipso.Jabberwalkie@company.com
# if we would have made email into a method then we would 
# have to use print(emp1.email()) instead of print(emp1.email) 
# so we turn a method into a variable with @property property Decorator
print(emp1.email)
print(emp1.fullname())
