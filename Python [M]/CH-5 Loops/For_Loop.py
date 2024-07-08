# For loop
# used for sequential traversal
'''
Syntax:
for variable in sequence:
    # Block of code to execute for each item in the sequence
'''

# Example-1 :
nums = [1, 2, 3, 4, 5]

for value in nums:
    print(value)
'''
Output:
1
2
3
4
5
'''
# Example-2 :
fav_food = ["Hyderabadi Biryani", "Butter chicken", "Italian margherita"]
for food in fav_food:
    print(food)
'''
Output:
Hyderabadi Biryani
Butter chicken
Italian margherita
'''

# Example-3 :
str = "RoyalEnfield"
for char in str:
    print(char)
'''
Output:
R
o
y
a
l
E
n
f
i
e
l
d
'''

# For loop with optional else:
'''
for element in list:
    # some work
else:
    # work, when for loop ends    
'''
# Example-1 :
nums = (2,4,6,8)
for value in nums:
    print(value)
else:
    print("Loop ended")
'''
Output:
2
4
6
8
Loop ended
'''

# Consider a program,
#1
str = "apnacollege"

for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)
else:                       #with else
    print("END")
'''
Output:
a
p
n
a
c
o found
'''

#2
str = "apnacollege"

for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)             #without else
print("END")
'''
Output:
a
p
n
a
c
o found
END
'''

#--------------------------------------------------------------------------------------------------------------------

# Practice Problems:

'''
Q1: print the elements of the following list using a loop
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
# Solution:
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in nums:
    print(i)
'''
Output:
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
Q2: Search for a number x in this tuple using loop
(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
'''
# Solution:
x = int(input("Enter key: "))
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
for i in nums:
    if i == x:
        print("Found")
        break
    else:
        print("Not Found")
'''
Output:
Enter key: 1
Found
'''
#--------------------------------------------------------------------------------------------------------------------

# range(): a bulit-in function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and stops before a specified number.
'''
Syntax: range(start?, stop, step?) 
*? =  optional
Examples:

range(10) #range(stop)
Output: 
0
1
2
3
4
5
6
7
8
9

range(2,10) #range(start,stop)
Output:
2
3
4
5
6
7
8
9

range(2,10,2) #range(start,stop,step)
Output:
2
4
6
8
'''

'''
Example-1: 
range(5)  returns the numbers from 0 to 4
which means,
Start = 0 (by default)
Stop = 5
Step = 1 (increments) (by default)
'''
# Example-2:
seq = range(5)

for i in seq:
    print(i) 
'''
Output:
0
1
2
3
4
'''
# simplier way writing the above logic
for i in range(5):
    print(1)
'''
Output:
0
1
2
3
4
'''
# Example-3: print even numbers from 50 to 60
for i in range(50,60,2):
    print(i)
'''
Output:
50
52
54
58
'''
# Example-4: print odd numbers from 95869 to 95877
for i in range(95869,95877,2):
    print(i)
'''
Output:
95869
95871
95873
95875
'''
#--------------------------------------------------------------------------------------------------------------------

# Practice programs

'''
Q1: Print numbers from 1 to 100
'''
# Solution:
for i in range(1,101):
    print(i)
# Output: 1 2 3 4 5.......99 100

'''
Q2: Print numbers from 100 to 1
'''
# Solution
for i in range(100,0,-1):
    print(i)
# Output: 100 99 98 97 96.......3 2 1

'''
Q2: Print the multiplication table of number n
'''
# Solution
n = int(input("Enter a number: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
'''
Output:
Enter a number:
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
#--------------------------------------------------------------------------------------------------------------------

# pass statement
# pass is a null statement that does nothing. It it used as a placeholder for future code.
'''
Syntax:
for el in range():
    pass
'''
# Example:
'''
for i in range(5):
    #empty
print(i)
'''
# Output: throws an error saying, that the print statement should be in an indented block.
# Solution:
for i in range(5):
    pass
print(i)
# Output: 0 1 2 3 4

#pass statement can also be used in if-else statements.

#--------------------------------------------------------------------------------------------------------------------

# Practice programs:

'''
Q1: WAP to find the sum of first n numbers
'''
# Solution: using for loop
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    sum += i
print("Sum of first",n,"numbers is:",sum)
# Output: Enter a number: 5
# Sum of first 5 numbers is: 15

'''
Q2: WAP to find the factorial of first n numbers
'''
# Solution:
n = int(input("Enter a number: "))
factorial = 1
for i in range(1,n+1):
    factorial *= i
print("Factorial of",n,"is:",factorial)
# Output: Enter a number: 5
# Factorial of 5 is: 120