# While loop:
# 1. It is used to execute a block of code multiple times.
# 2. It is used to execute a block of code until a certain condition is met.

# Syntax : 
'''
while condition:
    # code that need to be executed
'''
# Example 1 : Print 'Hello' 5 times
count = 1
while count <= 5:
    print('Hello')
    count += 1 # count = count + 1
# Output : Hello Hello Hello Hello Hello

'''
The 'count' variable used here is known as "iterator",
the processing of loops is known as "iteration".
'''

# Example 2 : Print 'Hello, World' 10000 times and display the no of iteration.
i = 1
while i <= 10000:
    print('Hello, World', i)
    i += 1 # i = i + 1
'''
Output :
Hello, World 1
Hello, World 2
Hello, World 3
.
.
.
.
Hello, World 9999
Hello, World 10000
'''

# Example 3 : Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1 # i = i + 1
# Output : 1 2 3 4 5

# Example 4 : Print numbers from 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1 # i = i - 1
# Output : 5 4 3 2 1

# Example 5 : Print even numbers from 1 to 10
i = 1
while i <= 10 :
    if (i%2==0) :
        print(i)
        i += 1
    else :
        i += 1
# Output : 2 4 6 8 10

#--------------------------------------------------------------------------------------------------------------------

# Practice programs

'''
Q1: Print numbers from 1 to 100.
'''
# Solution:
i = 1
while i <= 100 : 
    print(i)
    i += 1
# Output : 1 2 3 4 5 6 7 8....99 100

'''
Q2: Print numbers from 100 to 1.
'''
# Solution:
i = 100
while i >= 1 :
    print(i)
    i -= 1
# Output : 100 99 98 97 96 95 94 93.....2 1

'''
Q3: Print the multiplication table of number n
'''
# Solution:
n = int(input("Enter a number : "))
i = 1
while i <= 10 :
    print(n,"x",i,"=",n*i)
    i += 1
'''
Output :
Enter a number : 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''

'''
Q4: Print the elements of the following list using a loop
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
# Solution:
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i <= (len(list)-1): # or i < len(list)
    print(list[i]) # list[1], list[2], list[3],....list[(len(list)-1)]
    i += 1
# Output:
'''
1
4
9
16
25
36
49
64
81
100
'''

'''
Q5: Linear search 
Search for a number x in this tuple using loop
(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
'''

# Solution:
tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter key: "))
i = 0
while i < len(tuple):
    if tuple[i] == x:
        print("Found at index", i)
    else:
        print("finding..")
    i += 1

#--------------------------------------------------------------------------------------------------------------------

# Break & Continue:
'''
Break: It is used to terminate the loop.
Continue: It is used to skip the current iteration and continue with the next iteration.
'''

# Example program for Break statement: 
# Write a program to print the numbers from 1 to 10. Break at 5
# Solution:
i = 1
while i <= 10:
    print(i)
    if (i == 5):
        break
    i += 1
'''
Output:
1
2
3
4
5
'''

# Example program for Continue statement:
# Write a program to print the numbers from 1 to 10. Skip number 5
# Solution:
i = 1
while i <= 10:
    if (i == 5):
        i += 1
        continue # Acts as skip 
    print(i)
    i += 1
'''
Output: 
1
2
3
4
6
7
8
9
10
'''

# Example program for Continue Statement - 2 : print odd and even numbers
# Solution : printing odd numbers
i = 1
while i <= 10:
    if (i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1
'''
Output: 
1
3
5
7
9
'''

# Solution : printing even nnumbers
i = 1
while i <= 10:
    if (i % 2 != 0):
        i += 1
        continue
    print(i)
    i += 1
'''
Output: 
2
4
6
8
10
'''

#--------------------------------------------------------------------------------------------------------------------

# Practice programs:

'''
Q1: WAP to find the sum of first n numbers
'''
# Solution: using while loop
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum of first",n,"numbers is:",sum)
# Output: Enter a number: 5
# Sum of first 5 numbers is: 15

'''
Q2: WAP to find the factorial of first n numbers
'''
# Solution:
n = int(input("Enter a number: "))
factorial = 1
i = 1
while i <=n:
    factorial *= i
    i += 1
print("Factorial of",n,"is:",factorial)
# Output: Enter a number: 5
# Factorial of 5 is: 120