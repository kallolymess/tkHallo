class Empoyee():

#   Working with class variables
    num_of_emps = 0
    raise_ammount = 1.02

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Empoyee.num_of_emps += 1 # This is an example of a class variable where we would rather use 
        # Employee-Class rather than one of the instances


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

#   This is where we will use the Class variable
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_ammount)

#   This is where we will use the Class variable
    def apply_raise2(self):
        self.pay = int(self.pay * Empoyee.raise_ammount)


emp1 = Empoyee('Kallol', 'Biswas', 40000)
emp2 = Empoyee('Corey', 'Schafer', 50000)
emp3 = Empoyee('Test', 'User', 60000)

print(Empoyee.num_of_emps)