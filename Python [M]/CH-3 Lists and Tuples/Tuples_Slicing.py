# Tuples Slicing
'''
Similar to list slicing
Syntax: tuple_name[ Starting_index : Ending_index ] #Ending index not included, same as lists.
'''

# Example 1
my_tuple = (1, 2, 3, 4, 5, 6)
print(my_tuple[1:4])  # Output: (2, 3, 4)
print(my_tuple[ :4]) # Output: (1, 2, 3, 4) # Same as [0:4]
print(my_tuple[1: ]) # Output: (2, 3, 4, 5, 6) # Same as [1:len(my_tuple)]
print(my_tuple[-3:-1]) # Output (4,5) # Negative indexing same as lists