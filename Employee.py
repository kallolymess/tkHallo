class Empoyee():

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Empoyee('Kallol', 'Biswas', 40000)
emp2 = Empoyee('Corey', 'Schafer', 50000)
emp3 = Empoyee('Test', 'User', 60000)

print("With :- print(emp1.first + ' ' + emp1.last + ' : ' + emp1.email)")
print(emp1.first + ' ' + emp1.last + ' : ' + emp1.email)
print('\n')

print("print(emp2.fullname())")
print(emp2.fullname())
print('\n')

print("print(Empoyee.fullname(emp3))")
print(Empoyee.fullname(emp3))
