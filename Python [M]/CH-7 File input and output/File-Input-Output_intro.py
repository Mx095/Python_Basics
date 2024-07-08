# File I/O : Python can be used to perform operations on a file. (read & write data)
'''
Types of files:
1. Text files: .txt, .docx, .log etc.
2. Binary files: .mp4, .mov, .jpg, .png, .mp3, .exe etc.
'''
# Basic file manipulation operations in python:

# 1. Opening a file:-------------------------------------------------------------------------------------------------

'''
Syntax: f = open("file_name", "mode") 

file_name: name of the file 
Ex: sample.txt, demo.docx

mode: format of I/O operations (Whether we perform read or write)
Ex: r - read mode
    w - write mode
'''
# Example: 
#f = open("demo.txt", "r") # if in same folder, mentioning whole path isn't required.
#f = open("C:\\Users\\user\\Desktop\\demo.txt", "r")  # if not, mentioning path is required.

# 2. Reading a file:-------------------------------------------------------------------------------------------------
'''
Syntax: f.read()
'''
# Example:
f = open(r"C:\Users\samsu\OneDrive\Desktop\CODE\Python [M]\CH-7 File input and output\demo.txt", "r")
# 'r' before the entire path or use double slashes '\\' in place of single slashes '\' instead of using 'r'.
data = f.read()
print(data) 
# Output: I'm a student.
#         Vishnu Institute of Technology, Bhimavaram.
# Data present in the file
print(type(data)) # Output: <class 'str'>

# Passing parameters in read function.
# Example: 
f = open("demo.txt", "r")
data = f.read(5)
print(data) # Output: I'm a # Reads only 5 characters 

'''
To read file, line-by-line:
Syntax: f.readline()
'''
# Example:
f = open("demo.txt", "r")
line1 = f.readline()
print(line1) 
# Output: I'm a student.
#        (                                          ) # Empty space
# Reads only 1 line
# if there exists data more than a line, empty space is printed

'''
f = open("demo.txt", "r")

data = f.read()
print(data)

line1 = f.readline()
print(line1) 

line2 = f.readline()
print(line2)

Output :
I'm a student,
Vishnu Institute of Technology, Bhimavaram.

'''

# 3. Closing a file:-------------------------------------------------------------------------------------------------
# As a responsible programmers, if we open a file, we must also close the file. 
'''
Syntax: f.close()
'''
# Example:
f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()

#--------------------------------------------------------------------------------------------------------------------
'''
Different modes:
'r' -   open for reading(default)
'w' -   open for writing, truncating the file first
'x' -   create a new file and open it for writing
'a' -   open for writing,  appending to the end of the file if it exists
'b' -   binary mode
't' -   text mode(default) (implicit)
'+' -   open a disk file for updating (reading and writing)
'''
#--------------------------------------------------------------------------------------------------------------------

# 4. Writing to a file:---------------------------------------------------------------------------------------------
# Syntax: f.write(data)

# Example-1: Overwriting entire file
f = open("demo.txt", "w")
f.write("This is a new line") # Overwrites the entire file

# Example-2: Adds/ appends data to the existing data in the file
f = open("demo.txt", "a")
f.write("This is a new line") # Appends data to the existing data in the file

'''
If the file doesn't exists, "w" or "a" both will create the file in the same folder when the program is compiled.
'''

#--------------------------------------------------------------------------------------------------------------------

# "with" Syntax
'''
with open("demo.txt", "a") as f:
    data = f.read()
'''
# automatically closes the file, without using the closing function.

# Example-1: read mode
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

# Example-2: write mode
with open("demo.txt", "w") as f:
    f.write("This is a new line") # Overwrites the entire file

# 5. Deleting a file:------------------------------------------------------------------------------------------------
# using the "os" module
'''
Module (like a code library) is a file written by another programmer that generally has a functions we can use.
To install modules:
pip install module_name or pip3 install module_name
Example: pip install tensorflow (a module used in ML)
'''

'''
Syntax:
import os
os.remove(file_name)
'''
