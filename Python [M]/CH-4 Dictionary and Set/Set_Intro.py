# SETS : collection of unordered items, each element in the set must be unique & immutable.
'''
# Syntax : set_name = {element1, element2, element3,...}
# Sets are unindexed, so items in a set cannot be accessed by index.
# Sets are unchangeable (immutable), so you cannot change the items inside the set after you create it.
'''
# Elements can be of any data types
# Set1 = {1, 2, 3, "Hello", "World"}

# Set removes the duplicates in its elements
Set2 = {1, 2, 2, 2, 3, 4, "Hello", 'World', 'World'}
print(Set2) # Output : {1, 2, 3, 4, 'Hello', 'World'}

# Unordered items
Set3 = {1, 2, "Hello", "World", 4}
print(Set3) # Gives a random order of elements as output

# No of elements in the set :
Set4 = {1, 2, 2, 2, 3, 4}
print(len(Set4)) # Output : 4

# Empty set
Set5 = {}
print(type(Set5)) # Output : <class 'dict'> # Empty set is a dictionary in python
Set5 = set()
print(type(Set5)) # Output : <class 'set'> # Empty set is a set in