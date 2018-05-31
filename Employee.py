class Employee():

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
        
        Employee.num_of_emps += 1 

    def fullname(self): 
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_ammount)

    def apply_raise2(self):
        self.pay = int(self.pay * Employee.raise_ammount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_ammount = amount

    @classmethod
    def from_string(cls, emp_string):
# split the string 
        first, last, pay = emp_string.split('-')
# make new Employee with them
        return cls(first, last, pay)

emp1 = Employee('Kallol', 'Biswas', 40000)
emp2 = Employee('Corey', 'Schafer', 50000)
emp3 = Employee('Test', 'User', 60000)


# If we were to create Employee instances out of the THAT data we would have to do 
# something like set them to variables
emp_str1 = 'Jason-Bourn-40000'
emp_str2 = 'John-Doe-50000'
emp_str3 = 'Steve-Stoned-60000'
emp_str4 = 'Jane-Doe-50000'

# split the string 
first, last, pay = emp_str1.split('-')

# make new Employee with them
emp4 = Employee(first, last, pay)

# Test
print(emp4.__dict__)

# Troublesome and accident prone, Automation is the answer.

# So we make a new new Classmethod that returns a Employee when we feed it a string like John-Doe-50000
emp5 = Employee.from_string(emp_str2)
emp6 = Employee.from_string(emp_str3)
emp7 = Employee.from_string(emp_str4)
print(emp5.__dict__)
print(emp6.__dict__)
print(emp7.__dict__)

 