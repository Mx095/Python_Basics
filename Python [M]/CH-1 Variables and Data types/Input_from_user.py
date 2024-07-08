'''
input() statement is used to accept values from user 
'''

name = input ("Enter your name: ")
print("Welcome ", name)

# input() is always taken as a string 
age = input("Enter your age: ")
print("Your age is ", age)
print(type(age)) # gives output as str

# Here we need to do type casting 
age = int(input("Enter your age: "))
print("Your age is ", age)
print(type(age)) # gives output as int

# Same for float
height = float(input("Enter your height: "))
print("Your height is ", height)
print(type(height)) # gives output as float

