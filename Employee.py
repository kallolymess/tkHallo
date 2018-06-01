import datetime

class Employee():

# Static Methods : 
# Regular Methods pass an Instance as the first option, 
# Class Methods pass a Class as the first option, 
# Static Methods pass None
 
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
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

# They dont have a class or an instance as the first option
# They are mostly some function that is relevant to this Class and so its there.
# A sure way to know if you should use a Static Method instead of Class or Regular Method is
# to see if the 'cls' or 'self' is being referred to at all inside the method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('Kallol', 'Biswas', 40000)
emp2 = Employee('Corey', 'Schafer', 50000)
emp3 = Employee('Test', 'User', 60000)

emp_str1 = 'Jason-Bourn-40000'
emp_str2 = 'John-Doe-50000'
emp_str3 = 'Steve-Stoned-60000'
emp_str4 = 'Jane-Doe-50000'

first, last, pay = emp_str1.split('-')
emp4 = Employee(first, last, pay)
print(emp4.__dict__)

emp5 = Employee.from_string(emp_str2)
emp6 = Employee.from_string(emp_str3)
emp7 = Employee.from_string(emp_str4)
print(emp5.__dict__)
print(emp6.__dict__)
print(emp7.__dict__)

my_date = datetime.date(2016, 7, 11)
# Calling a static method.
print(Employee.is_workday(my_date))

# on a sidenote the imported datetime module, datetime.py will convert a lot of 
# different ways of date expressions, that is being done with multiple Constructors 
# similar to what we have here as second Constructor 'from_string'