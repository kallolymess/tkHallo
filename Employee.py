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

# getters, setter : getters are done with @property and @setters are done with @<Variable>.setter
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleting {} : {}'.format(self.fullname, self.email))
        self.first = None
        self.last = None

emp1 = Employee('Robertsonn', 'Jabberwalkie', 40000)

emp1.fullname = 'Messi Andriotti'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

# Deleter is called with a del
del emp1.fullname

print(emp1.first)
print(emp1.email)
print(emp1.fullname)
