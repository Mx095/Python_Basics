# Tuples : A built in data type lets us create immutable sequence of values.
#          properties similar to strings.
# Syntax : tuple_name = (element1, element2, element3, element4,...)
# Enclosed by parenthesis '()'

'''
Example:
my_tuple = (1, 2, 3, 4, 5)
print(type(my_tuple))  # Output: <class 'tuple'>
'''

# Empty tuple -> tup = ()
# Single valued tuple -> tup = (1,) # comma necessary
# if comma doesn't exist, Python will consider is as an integer 
'''
Example: 
tup = (1,)
print(type(tup))  # Output: <class 'tuple'>
tup = (1)
print(type(tup))  # Output: <class 'int'>
'''
# in case of multiple elements, comma after the last element is not necessary.

# Accessing elements in tuple -> same as lists
'''
Example:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 5
'''
