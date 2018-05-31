class Empoyee():

# This time we are all about Regular methods, Class methods and Static Methods
#  
    num_of_emps = 0
    raise_ammount = 1.02

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Empoyee.num_of_emps += 1 

# Regular Method : it has (self) (instance) as the first argument
    def fullname(self): 
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_ammount)

    def apply_raise2(self):
        self.pay = int(self.pay * Empoyee.raise_ammount)

# Class Method : To have a (class) as the first argument we use a decorator @staticmethod before the method 
    @staticmethod
    def set_raise_amt(cls, amount):
        cls.raise_ammount = amount

emp1 = Empoyee('Kallol', 'Biswas', 40000)
emp2 = Empoyee('Corey', 'Schafer', 50000)
emp3 = Empoyee('Test', 'User', 60000)

# this will create some problems in the long run if we are not careful.
# we have decided that emp1 will have an explicit value of raise_ammount
emp1.raise_ammount = 1.55
print(Empoyee.raise_ammount)
print(emp1.raise_ammount)
print(emp2.raise_ammount)
print(emp3.raise_ammount)
print('------------------------------')
# calling a Class Method to change the Class Variable
Empoyee.set_raise_amt(Empoyee, 1.33) 
print(Empoyee.raise_ammount) 
# Can you see the problem ... since we had set emp1.raise_ammount we have 
# a Instance Variable value and not Class Variable value when the Class Variable is changed
print(emp1.raise_ammount)
print(emp2.raise_ammount)
print(emp3.raise_ammount)
print('------------------------------')
emp1.raise_ammount = Empoyee.raise_ammount
print(emp1.raise_ammount)
print('------------------------------')
# We see that the Class Variable being available to an instance explicitely can cause a bit of confusion
# if we dont pay attention  
print(emp1.__dict__)
print('------------------------------')
print(emp2.__dict__)
print('------------------------------')

# Summary: So the difference bet. Class method and Regular method is what they accept as their first arg.
# got some intro go decorators ... @staticmethod and basic conventions like "self" and "cls" we can use 
# any word in their places, but its cleaner to stick to the convention. Tip: we cant use the word "class"
# instead of "cls". because "class" is a unique word for Python
# 