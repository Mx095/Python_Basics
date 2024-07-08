# Practice programs: Dictionaries & Sets

'''
Q1: Store the following  word meanings in a python dictionary :
Table : "a piece of furniture", "list of facts & figures"
cat : "a small animal"
'''
# Solution: 
dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}
print(dictionary)
# Output: {'cat': 'a small animal', 'table': ['a piece of furniture', 'list of facts & figures']}

'''
Q2: You are given a list of subjects for students. Assume one class is required for 1 subject.
How many classrooms are needed by all students.
"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
'''
# Solution:
subjects = {
"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
}
print(len(subjects))
# Output: 5
# 5 classrooms are needed by all students

# Note: Python will consider "C++" and "c++" as two different elements. Hence, input must be given as either "C++"
# or "c++". if not, these will get considered as two different elements and required solution may vary.

'''
Q3: WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary
and add one by one. Use subject name as key and marks as value.
'''
# Solution:
marks = {}

x = int(input("Enter Maths marks: "))
marks.update({"Maths" : x})

x = int(input("Enter Physics marks: "))
marks.update({"Physics" : x})

x = int(input("Enter Chemistry marks: "))
marks.update({"Chemistry" : x})

print(marks)
# Output: {'Maths': 90, 'Physics': 80, 'Chemistry': 70}
# marks given as input by the user.

'''
Q4: Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)
'''
# Solution:
set1 = {9, 9.0}
print(set1) # Output = {9}
# Note: Python will consider 9 and 9.0 as same element.

# Possible way of solution-1: Type casting
set1 = {9,"9.0"} 
print(set1) # Output = {9, '9.0'} 

#Possible way of solution-2:
set1 = {
    ("float", 9.0),
    ("int", 9)
}
print(set1) # Output = {('float', 9.0), ('int', 9)}

# Possible way of solution-3:
set1 = {9, float("9.0")}
print(set1) # Output = {9, 9.0}