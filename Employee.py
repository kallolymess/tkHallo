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

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--> ', emp.fullname())

# Test Subclassing
emp1 = Developer('Kallol', 'Biswas', 40000, 'python')
emp2 = Developer('Corey', 'Schafer', 50000, 'Java')
emp3 = Employee('Dave', 'Dey', 60000)
            
mgr_1 = Manager('Trudy', 'Manager', 80000, [emp1])

print(mgr_1.email)
mgr_1.add_emp(emp2)
mgr_1.add_emp(emp3)
mgr_1.print_emps()
print('-------')
mgr_1.remove_emp(emp3)
mgr_1.print_emps()

print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Employee, Developer))
print(issubclass(Developer, Employee))
