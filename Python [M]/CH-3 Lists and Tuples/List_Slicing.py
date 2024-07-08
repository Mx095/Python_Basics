# List Slicing
'''
Similar to string slicing
Syntax: list_name[ Starting_index : Ending_index ] #Ending index not included, same as strings.
'''

# Example-1
marks = [87, 64, 33, 95, 76]
print(marks[1:4])  # Output: [64, 33, 95]
print(marks[ :4]) # Output: [87, 64, 33, 95] # Same as [0:4]
print(marks[1: ]) # Output: [64, 33, 95, 76] # Same as [1:len(marks)]
print(marks[-3:-1]) # Output [33,95] # Negative indexing same as strings