class Empoyee():

#   Working with class constants
    raise_ammount = 1.02

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

#   This is where we will use the Class Constant
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_ammount)

#   This is where we will use the Class Constant
    def apply_raise2(self):
        self.pay = int(self.pay * Empoyee.raise_ammount)


emp1 = Empoyee('Kallol', 'Biswas', 40000)
emp2 = Empoyee('Corey', 'Schafer', 50000)
emp3 = Empoyee('Test', 'User', 60000)

# Some Tests to show what the difference it makes  if we use 
# Employee.raise_ammount to self.raise_ammout in the apply_raise function
print('emp1.raise_ammount : ' + str(emp1.raise_ammount) + ',   emp2.raise_ammount : ' + str(emp2.raise_ammount) + ',   emp3.raise_ammount : ' + str(emp3.raise_ammount))

# __dict__ is a cool function that lists out all attributes and values of a class
print(' \n --- \n' + str(Empoyee.__dict__) + ' \n --- \n')
print(str(emp1.__dict__) + ' \n --- \n')

# now if I increase the raise_ammount for one Employee 
emp1.raise_ammount += 0.03

print(' \n --- \n' + str(Empoyee.__dict__) + ' \n --- \n')
print(str(emp1.__dict__) + ' \n --- \n')

emp1.apply_raise2()
print('emp1.raise_ammount : ' + str(emp1.raise_ammount) + ',   emp2.raise_ammount : ' + str(emp2.raise_ammount) + ',   emp3.raise_ammount : ' + str(emp3.raise_ammount))
print('emp1.pay : ' + str(emp1.pay) + ',   emp2.pay : ' + str(emp2.pay) + ',   emp3.pay : ' + str(emp3.pay))

print(' \n --- \n' + str(emp1.__dict__) + ' \n --- \n')
print(str(emp2.__dict__) + ' \n --- \n')

emp1.pay = 40000
emp1.apply_raise()
print('emp1.raise_ammount : ' + str(emp1.raise_ammount) + ',   emp2.raise_ammount : ' + str(emp2.raise_ammount) + ',   emp3.raise_ammount : ' + str(emp3.raise_ammount))
print('emp1.pay : ' + str(emp1.pay) + ',   emp2.pay : ' + str(emp2.pay) + ',   emp3.pay : ' + str(emp3.pay))

print(' \n --- \n' + str(Empoyee.__dict__) + ' \n --- \n')
print(str(emp1.__dict__) + ' \n --- \n')

# So summary: when we initiate an instance eg: emp1
# it wont have an explicit Class Constant attached to it 
#       - from output lookout for the missing raise_ammout for Kallol Biswas in the beginning 
