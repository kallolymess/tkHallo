courses = ['Math', 'Physics', 'History', 'CompSci', 'Biology']

# joining
courses_str = ' - '.join(courses)
print(courses_str)

# splitting
new_list = courses_str.split(' - ')
print(new_list)
# for item in courses:
#     print(item)

# Enumerate(pimping the lists with numbers)
# indexes can be extracted to a seperate variable
# the start value of the list can be set in python

# for index, course in enumerate(courses, start=2):
#     print(index, course)


# print(courses.index('History'))

# nums = [11, 2, 9, 88, 4, 32]

# print(nums)
# print(sorted(nums))
# print(sum(nums))
# print(min(nums))
# print(max(nums))

# sorted(courses)
# print(courses)
# print(sorted(courses))
# print(courses)

# slicing
# print(courses[1:2])
# print(courses[2:])

# courses.append('Art')
# courses.insert(2, 'Commerce')
# print(courses)
# courses.remove('History')
# print(courses)

# courses.sort()
# print(courses)

# courses.reverse()
# print(courses)
