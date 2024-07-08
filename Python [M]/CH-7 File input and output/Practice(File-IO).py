# Practice programs: File I/O

'''
Q1: Create a new file "practice.txt" using python. add the following data in it:
    Hi everyone
    we are learning File I/O
    using Python
    I like programming in python
'''
# Solution:
with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Python\nI like programming in python\n")

'''
Q2: WAF that replaces all occurences of "Python" with "Java" in above file.
'''
# Solution:
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Python", "Java")
with open("practice.txt", "w") as f:
    f.write(new_data)
'''
Output:
    Hi everyone
    we are learning File I/O
    using Java
    I like programming in Java
'''

'''
Q3: Search if the word "learning" exists in the file or not.
'''
# Solution:
word = "learning"
with open("practice.txt", "r") as f:
   data = f.read()
   if(data.find(word) != -1):
       print("Found")
   else:
       print("Not Found")

# Output:  Found

'''
Q4: WAF to find in which line of the file does the word "learning" occur first. Print -1 if word not found.
'''
# Solution:

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

check_for_line() # Output: 2

'''
Q5: From a file containing numbers separated by comma, print the count of even numbers.
Data in "practice.txt" file:
1, 2, 76, 84, 90, 101
'''
# Solution:
count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count) # Output: 3