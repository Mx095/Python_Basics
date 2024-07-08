# Set functions
'''
Sets -> mutable
Elements in the set -> immutable
'''
# 1. set.add(element)------------------------------------------------------------------------------------------------
# adds an element
Set1 = set()
Set1.add(1)
Set1.add(2)
Set1.add(2)
Set1.add(3)
print(Set1) # Output : {1, 2, 3}

'''
We can add elements such as strings, tuples which are IMMUTABLE in the set as elements.
IMMUTABLE ELEMENTS can generate hash values, (Hashable = Immutable)
Whereas Mutable elements such as Lists cannot.
Adding list as an element throws an 'typerror: unhashable type: 'list'
'''

# 2. set.remove(element)------------------------------------------------------------------------------------------------
# removes an element
Set2 = {1, 2, 3}
Set2.remove(2)
print(Set2) # Output : {1, 3}

# removing a non-existing element :
Set2.remove(4) # Throws an error

# 3. set.clear()-----------------------------------------------------------------------------------------------------
# empties the set
Set3 = {1, 2, 3}
print(len(Set3)) # Output = 3
Set3.clear()
print(len(Set3)) # Output = 0

# 4. set.pop()-------------------------------------------------------------------------------------------------------
# removes and returns a random element in the set
Set4 = {"Hello", "World", 1, 2, 3}
print(Set4.pop()) # Output : 1 or 2 or 3 or "Hello" or "World"

# 5. set.union(set2)-------------------------------------------------------------------------------------------------
# combines both set values and returns a new one
Set1 = {1, 2, 3}
Set2 = {3, 4, 5}
print(Set1.union(Set2)) # Output : {1, 2, 3, 4, 5}

# 6. set.intersection(set2)------------------------------------------------------------------------------------------
# returns a new set with common elements in both sets
Set1 = {1, 2, 3}
Set2 = {3, 4, 5}
print(Set1.intersection(Set2)) # Output : {3}