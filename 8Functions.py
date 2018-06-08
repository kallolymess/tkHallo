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

student_info(*courses, **info)

# output: 
# (venvTKinter) λ python 8Functions.py
# ('Biology', 'Chem', 'CompSci')
# {'first': 'Carlos', 'last': 'Benini', 'age': 33}
