class Empoyee():

#  How class methods can be used a new Constructor
# Take for instance if we get the data about a new employee in the form 
# Jason-Bourn-40000, John-Doe-50000, Steve-Stoned-60000, Jane-Doe-50000
 
    num_of_emps = 0
    raise_ammount = 1.02

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Empoyee.num_of_emps += 1 

    def fullname(self): 
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_ammount)

    def apply_raise2(self):
        self.pay = int(self.pay * Empoyee.raise_ammount)

    @staticmethod
    def set_raise_amt(cls, amount):
        cls.raise_ammount = amount

emp1 = Empoyee('Kallol', 'Biswas', 40000)
emp2 = Empoyee('Corey', 'Schafer', 50000)
emp3 = Empoyee('Test', 'User', 60000)


# If we were to create Employee instances out of the THAT data we would have to do 
# something like set them to variables
emp_str1 = 'Jason-Bourn-40000'
emp_str2 = 'John-Doe-50000'
emp_str3 = 'Steve-Stoned-60000'
emp_str4 = 'Jane-Doe-50000'

# split the string 
first, last, pay = emp_str1.split('-')

# make new Employee with them
emp4 = Empoyee(first, last, pay)

# Test
print(emp4.__dict__)

# Troublesome and accident prone, Automation is the answer.

 