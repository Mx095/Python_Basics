'''
A+B -> here A,B are operands and + is operator
Types of operators:
1. Arithmetic operators: (+,-,*,/,%,**)
2. Comparison operators: (==,!=,>,<,>=,<=) 
3. Assignment operators: (=,+=,-=,*=,/=,%=,//=,**=)
4. Logical operators: (and,or,not)
'''

# Arithmetic operators----------------------------------------------------------------------------------------------
a = 10
b = 5
print("Addition: ", a + b)
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)
print("Modulus: ", a % b) #remainder
print("Exponential: ", a ** b) #power

# Comparison / Relational operators--------------------------------------------------------------------------------- 
a = 10
b = 5
print("Equal: ", a == b) #output = False
print("Not Equal: ", a != b) #output = true
print("Greater than: ", a > b) #output = true
print("Less than: ", a < b) #output = false
print("Greater than or equal to: ", a >= b) #output = true
print("Less than or equal to: ", a <= b) #output = false

# Assignment operators----------------------------------------------------------------------------------------------
# =
a = 10
print("Value of a: ", a)

# +=
num = 20
num += 10 #num = num + 10
print("Value of num: ", num) # 20+10=30

# -=
num = 30
num -= 10 #num = num - 10
print("Value of num: ", num) # 30-10=20

# *=
num = 20
num *= 2 #num = num * 2
print("Value of num: ", num) # 20*2=40

# /=
num = 20
num /= 2 #num = num / 2 
print("Value of num: ", num) # 20/2=10

# %=
num = 20
num %= 3 #num = num % 3
print("Value of num: ", num) # 20%3=2

# **=
num = 2
num **= 3 #num = num ** 3
print("Value of num: ", num) # 2**3=8

# Logical opeerators------------------------------------------------------------------------------------------------

# not operator :

#Example-1
print(not false) #output = true
print(not true) #output = false

#Example-2
a=50
b=30
print(not (a>b)) #output = false

# and operator :
print(true and true) #output = true
print(true and false) #output = false
print(false and true) #output = false
print(false and false) #output = false

# or operator :
print(true or true) #output = true
print(true or false) #output = true
print(false or true) #output = true
print(false or false) #output = false