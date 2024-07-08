'''
String is a data type that stores a sequence of characters
Ex: str1 = "This is a string."
'''

'''
Escape sequence characters: 
1. \n - new line
Ex: str1 = "This is a string.\nWe created this in python."
output:
This is a string.
We created this in python.

2. \t - tab space
Ex: str1 = "This is a string.\tWe created this in python."
output:
This is a string.   We created this in python.
'''

# Basic operation in strings

# 1. Concatenation
# "Hello" + "World" --> "HelloWorld"
str1 =  "Hello"
str2 = "World"
final_str = str1+str2
print(final_str)
# output: HelloWorld

# 2. Length of string
# prints length of the the string
str = "Python"
length = len(str)
print(length)
# output: 6