# Practice problems : Recursions

'''
Q1: Write a recursive function to calculate the sum of first n natural numbers.
'''
# Solution:
def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) + n
n=5
sum = calc_sum(n)
print(f"The sum of first {n} natural numbers is: ",sum)
# Output: The sum of first 5 natural numbers is:  15
'''
from BlackBox AI Chat: 
The f thing you're referring to is called an f-string.
It's a new way of formatting strings in Python,
introduced in version 3.6.
The f before the string indicates that it's an f-string.

In the first code snippet, the print statement is:
print(f"The sum of first {n} natural numbers is: ",sum)

Here, f"The sum of first {n} natural numbers is: " is an f-string.
The {n} inside the string is a placeholder for the value of n.
When the string is formatted, the value of n is inserted in place of {n}.

So, if n is 5, the formatted string would be:
"The sum of first 5 natural numbers is: "

to summarize:

F-strings:
(like f"The sum of first {n} natural numbers is: "):
{n} is a placeholder for the value of n.

Regular strings:
(like "The sum of first {n} natural numbers is: "):
{n} is a literal {n}, not a placeholder.
'''

'''
Q2: Write a function to print all the elements in a list.
Hint: use list & index as parameters.
'''
# Solution:
def print_list(list, index=0): # Given default parameter
    if(index == len(list)):
        return
    print(list[index])
    print_list(list,index+1) #Updation

Numbers=[169, 269, 369, 469, 569]
print_list(Numbers) # Output: 169 269 369 469 569