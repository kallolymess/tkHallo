# Tuples : they are lists that are not mutable ie. immutable lists
# what is meant by mutable?

list1 = ['Math', 'Physics', 'History', 'CompSci', 'Biology']
list2 = list1

print(list1)
print(list2)

list2.append('Art')
list2[3] = 'Neurobiology'

print(list1)
print(list2)

# ['Math', 'Physics', 'History', 'CompSci', 'Biology']
# ['Math', 'Physics', 'History', 'CompSci', 'Biology']
# ['Math', 'Physics', 'History', 'CompSci', 'Biology', 'Art']
# ['Math', 'Physics', 'History', 'CompSci', 'Biology', 'Art']

# Mutable : when we change the value of one list the Mutable list is updated to be exactly like the first

# Tuples are immutable
tuple1 = ('Math', 'Physics', 'History', 'CompSci', 'Biology')
tuple2 = tuple1

print(tuple1)
print(tuple2)

# tuple2[4] = 'Chem' Something like this will not function with Tuples cause they are Immutable.

print(tuple1)
print(tuple2)

# So tuples are good if we need a list to read and not edit