def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# student_info('Math', 'Art', name='John', age=22)

# output : 
# ('Math', 'Art') --> the 'args' with one * produces a Tuple 
# {'name': 'John', 'age': 22} --> the 'kwargs' with two ** produces a dictionary
# The words 'args' and kwargs are simply conventions. 
# We can name the parameters anything we like are simply conventions.

# Now we are going to use a more expressive parameters

courses = ['Biology', 'Chem', 'CompSci']
info = {'first': 'Carlos', 'last': 'Benini', 'age': 33}

# student_info(courses, info) 
# output: 
# (['Biology', 'Chem', 'CompSci'], {'first': 'Carlos', 'last': 'Benini', 'age': 33})
# {}
# --> wont work

# student_info(*courses, **info)

# output: 
# (venvTKinter) λ python 8Functions.py
# ('Biology', 'Chem', 'CompSci')
# {'first': 'Carlos', 'last': 'Benini', 'age': 33}

# some reallife implementations
# https://github.com/python/cpython/blob/master/Lib/datetime.py 
# Edited from _DAYS_IN_MONTH, def _is_leap(year):, def _days_in_month(year, month):

_DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def _is_leap(year):
    "year -> 1 if leap year, else 0."
    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def _days_in_month(year, month):
    "year, month -> number of days in that month in that year."
    
    """this 'assert' bit corresponds to 
    if not 1 <= month <= 12:
        return 'Invalid Month'
    """
    assert 1 <= month <= 12, month 

    if month == 2 and _is_leap(year):
        return 29
    
    return _DAYS_IN_MONTH[month]

print(_is_leap(2017))
print(_is_leap(2020))

print(_days_in_month(2017, 2))
print(_days_in_month(2020, 2))

