'''
Slicing:
- Slicing is a way to access elements
- It allows you to access elements of a sequence by their index
- The syntax for slicing is :
  str[ starting_index : ending_index ] #Ending index is not included
'''
str = "Hello, World!"
print(str[0:5]) #Hello
print(str[1:4]) #ell
print(str[0:6]) #Hello,
print(str[0:7]) #Hello, #(space also included)
print(str[7:]) #World! #[7:len(str)]
print(str[:5]) #Hello #[0:5]

# Slicing through Negative indexing 
str = "Apple"
str[-3:-1] #pl
'''
Here syntax runs the same :
str[starting_index : ending_index]
From the above example
str[-3:-1] means :
- starting_index = -3 (from the end of the string)
- ending_index = -1 (from the end of the string)
and -1 (ending index) is not included same as positive indexing 
'''
