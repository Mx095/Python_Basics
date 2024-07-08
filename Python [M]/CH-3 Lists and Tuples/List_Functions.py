# List functions

# 1. list.append(_)-------------------------------------------------------------------------------------------------
# Adds an element at the end of the list
my_list = [1, 2, 3, 4, 5]
# print(my_list.append(6)) will not work, will not return any value.
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# 2. list.sort()----------------------------------------------------------------------------------------------------
# Sorts the list in ascending order
my_list = [5, 2, 8, 1, 9]
# print(my_list.sort()) will not work, will not return any value.
my_list.sort()
print(my_list)  # Output: [1, 2, 5, 8, 9]

# Ascending order sorting can also be done in strings 
my_list = ['banana', 'apple', 'date', 'cherry']
my_list.sort()
print(my_list)  # Output: ['apple', 'banana', 'cherry', 'date']


# 3. list.sort(reverse=True)----------------------------------------------------------------------------------------
# Sorts the list in descending order
my_list = [5, 2, 8, 1, 9]
# print(my_list.sort(reverse=True)) will not work, will not return any value.
my_list.sort(reverse=True)
print(my_list)  # Output: [9, 8, 5, 2, 1]

# Descending order sorting can also be done in strings 
my_list = ['banana', 'apple', 'date', 'cherry']
my_list.sort()
print(my_list)  # Output: ['date', 'cherry', 'banana', 'apple']

# 4. list.reverse()-------------------------------------------------------------------------------------------------
# Reverses the order of the list
my_list = [9, 2, 8, 4, 7]
# print(my_list.reverse()) will not work, will not return any value.
my_list.reverse()
print(my_list)  # Output: [7, 4, 8, 2, 9]

# 5. list.insert(index, element)------------------------------------------------------------------------------------
# Similar to append, but inserts an element at a specified position or index in the list
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 6)
print(my_list)  # Output: [1, 2, 6, 3, 4, 5]

# 6. list.remove(element)-------------------------------------------------------------------------------------------
# Removes the first occurrence of the specified element in the list
my_list = [1, 2, 3, 4, 5, 2]
my_list.remove(2)   
print(my_list)  # Output: [1, 3, 4, 5, 2]

# 7. list.pop(index)-------------------------------------------------------------------------------------------------
# Removes the element at the specified position or index in the list and returns it
my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop(2)
print(my_list)  # Output: [1, 2, 4, 5]
print(popped_element)  # Output: 3
# If index is not specified, it removes and returns the last element in the list
my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop()
print(my_list)  # Output: [1, 2, 3, 4]
print(popped_element)  # Output: 5

# 8. list.index(element)-------------------------------------------------------------------------------------------
# Returns the index of the first occurrence of the specified element in the list
my_list = [1, 2, 3, 4, 5, 2]
index = my_list.index(2)
print(index)  # Output: 1