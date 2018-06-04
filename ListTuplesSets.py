# Sets : Lists that automatically throw away duplicates and is not ordered in any manner
# they are optimized to work faster for comparision.

set1 = {'His', 'Hers', 'Its', 'Ours', 'Yours', 'Theirs'}
print(set1)
set1.add('Hallo')
print(set1)
set1.add('Yours')
print(set1)

set2 = {'His', 'Whats', 'Its', 'Up', 'Yours', 'Doc'}
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))

# creating empty sets has a oopsie
# empty list and tuples can be created in two manners
emt_list = []
emt_list = list()

emt_tuple = ()
emt_tuple2 = tuple()

# butttt a set can only be created with the explicite call of set()

emt_set = {}  # This creates a Dictionary instead of a Set
emt_set1 = set()
