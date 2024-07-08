# Functions: Block of statements that perform a specific task.
# In other words, if a block of code is repeating again and again over the entire code, then functions are used for those redudant lines.
# Functions are defined using "def" keyword.
# Functions are called using function_name() syntax.
# Functions can return values using return keyword.
# Functions can take arguments using parameter syntax.
# Functions can have default values for parameters.
# Functions can have variable number of arguments using *args and **kwargs syntax.

'''
Syntax:
def function_name(parameter1, parameter2, ...):
    # function body
'''
# Example: sum of two numbers
a = int(input())
b = int(input())
def sum(a, b):
    return a + b
print(sum(a, b))

'''
function definition: def func_name(parameter1, parameter2,...)
function call:           func_name(arguement1, arguement2,...)
for example: 
def sum(a, b): #function definition
sum(1, 2) #function call
*arguements gets stored in the parameters
i.e, 1 gets stored in 'a' and 2 gets stored in 'b'.
'''
#--------------------------------------------------------------------------------------------------------------------

# Use of funtions?
# To avoid code redundancy.
# Example :
'''
We need to write a large code in which we need to perform 'addition of two numbers' 
for 5 times 
i.e,
'''

a = 5
b = 10
sum = a + b
print(sum)

# more lines of code

a = 2
b = 3
sum = a + b
print(sum)

# more lines of code

a = 15
b = 20
sum = a + b
print(sum)

# more lines of code

a = 39
b = 40
sum = a + b
print(sum)

# more lines of code

a = 95
b = 100
sum = a + b
print(sum)

# Instead of writing like this we can create functions and use them.
# This is called 'code reusability'.
# Example :
'''
We need to write a large code in which we need to perform 'addition of two numbers' 
for 5 times using functions
'''

def add(a,b): 
    sum = a + b
    return sum

print(add(5,10))
# more lines of code
print(add(2,3))
# more lines of code
print(add(15,20))
# more lines of code
print(add(39,40))
# more lines of code
print(add(95,100))

#--------------------------------------------------------------------------------------------------------------------

# function terminology:

#function definition
def add(a,b): # a,b -> parameters
    return a + b
sum = add(1,2) # function call; 1,2 -> arguements
print(sum)

#--------------------------------------------------------------------------------------------------------------------

# Functions can be given with no parameter or return value.
# For example: function that prints 'Hello', whenever it's called.
def print_hello(): # No parameter
    print("Hello") # No return value 

# Since the above function has no return value, it gives None as output
xyz = print_hello()
print(xyz) # Output = None

#--------------------------------------------------------------------------------------------------------------------

'''
Functions - 2 types
1. Built-in functions:
   These are the functions that are already defined in python.
2. User-defined functions:
   These are the functions that are defined by the user.
'''
# Built-in functions:------------------------------------------------------------------------------------------------
# print(), input(), len(), max(), min(), type(), range() etc.

# Overview of print() function: by hovering the print() function
'''
(function) def print(
    *values: object,
    sep: str | None = " ", #separator parameter
    end: str | None = "\n", #ending parameter
    file: SupporstWrite[str] | None = None,
    flush: Literal[False] = False
) -> None # return value
'''
# These are pre-defined in print() function in python.

# sep -> separator: if multiple are given with comma in between as an input, Space is occured in between two values
print("Lightning","Mcqueen") #sep =" "; separator is automatically defined as " " (space)
# Output : Lightning Mcqueen

# end -> ending: after printing once (using print function once), if we print again (use print function again), print those in next line
print("Lightning")
print("Mcqueen") #end = "\n"; end is automatically defined as "\n" 
# Output : Lightning
#          Mcqueen
# We can modify end parameter:
print("Lightning",end=" ")
print("Mcqueen") # Output : Lightning Mcqueen

# We can also modify sep parameter:
print("Lightning","Mcqueen",sep="$")
# Output : Lightning$Mcqueen

# User Defined functions:--------------------------------------------------------------------------------------------
# We can define our own functions in python.
'''
Syntax: def function_name(parameters):
            function body
            return value
            function_name() # calling the function
'''
'''
#Example: def add(a,b):
           return a+b
           add(2,3) # calling the function
           print(add(2,3)) # Output : 5
           print(add(2,3)+add(3,4)) # Output : 14
'''

# Default parameters:------------------------------------------------------------------------------------------------
# Assigning a default value to parameter, which is used when no arguement is passed.

# For example : a function to multiply to numbers
def product(a, b):
    return a*b
print(product(2,3)) # Output : 6

# If no arguements are given, i.e, no values are given:
print(product()) # Output : TypeError: product() missing 2 required positional arguments: 'a','b'

# In this case we give default parameters, which are used when no arguements are passed
def product(a=1, b=1): # providing default parameters
    return a*b
print(product()) # Output : 1

# Single default psrameter can also be passed, but on one condition:
# Non default arguement follows default arguement

# Correct way:
def product(a, b=2):
    print(a * b)
    return a * b
product(1) # 1 is passed as an arguement, gives the output : 2

# Incorrect way:
'''
def product(a=1, b):
    print(a * b)
    return a * b
product(2) # Throws an error
'''