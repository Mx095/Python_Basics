# LIST : A built-in data type that stores set of values
#        A built in data type lets us create mutable sequence of values.
# Syntax : list_name = [element1, element2, element3, element4,...] 
# Enclosed by square brackets '[]'
'''
for example:
instead of writing like this: 
marks1 = 95.0
marks2 = 95.1
marks3 = 95.3
marks4 = 95.4
marks5 = 95.5
we can make a list of marks like this: 
marks = [95.0, 95.1, 95.3, 95.4, 95.5]
print(type(marks)) # prints  <class 'list'>
'''
# Accessing elements in lists:
'''
marks = [87, 64, 33, 95, 76]
print(marks[0]) # prints 87
print(marks[1]) # prints 64
and so on
'''

# length of string can be printed --> len(list_name)

'''
In Python, List can store elements of different data types(int, float, string, etc.),
unlike any other programming languages.
Example:
student = ["Maha", 18, "Delhi", 95.95]
Here,
Maha -> string
18 -> integer value
Delhi -> string
95.95 -> float value
'''

'''
Difference between Strings and Lists
- Strings are immutable --> can access elements but cannot modify 
- Lists are mutable --> can acccess and modify

Example:
-------In Strings-------
name = "Maha"
print(name[0]) # prints M
name[0] = "A" # TypeError: 'str' object does not support item assignment

-------In Lists-------
name = ["M", "A", "H", "A"]
print(name[0]) # prints M
name[0] = "A" # works fine
'''

#Note: 
'''
In a list;
Student = ["Maha", 18, "Delhi", 95.95]
            0       1     2       3
List size is 4 which means the last index is 3.
If we try to add elements such a way that:
Student[4] = "New Delhi"
It will show an error because the list size is 4 and we are trying to access the
5th index which is out of range.
'''