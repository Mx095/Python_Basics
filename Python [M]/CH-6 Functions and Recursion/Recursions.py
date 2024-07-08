# Recursion : When a function calls itself repeatedly. 
'''
Example: WAF that prints n to backwards
'''
# Solution: 
def print_backwards(n):
    if n == 0:
        return # doesn't return any value, returns control
    print(n, end=' ')
    print_backwards(n-1)

print_backwards(5) # Output: 5 4 3 2 1 
print(end="\n") # for next program's output
'''
Explaination: 
Step-1: Input: 5
Step-2: print_backwards(5) is called, printed 5, then again called with (n-1) as parameter.
Step-3: print_backwards(4) is called, printed 4, then again called with (n-1) as parameter.
Step-4: print_backwards(3) is called, printed 3, then again called with (n-1) as parameter.
Step-5: print_backwards(2) is called, printed 2, then again called with (n-1) as parameter.
Step-6: print_backwards(1) is called, printed 1, then again called with (n-1) as parameter.
Step-7: print_backwards(0) is called, checks the if condition given, and recursion gets stopped.
'''

# In a recursive function, there must be a "base case" (condition) which breaks the recursion and returns.
# Same as stopping conditions in loops.
# If there is no base case, recursions run infinitely.

'''
Call stack:
When a function is called, it is pushed onto the call stack.
When the function returns, it is popped off the call stack.
The call stack is a LIFO (last in, first out) data structure.
When a function calls itself, it is pushed onto the call stack twice.
When the function returns, it is popped off the call stack twice.
'''
# Example-2: Explaining recursion through factorials
# WAF to find factorial of a number.
# Solution:
'''
Putting aside exceptional cases 0! and 1! which both are equal to 1,
factorial of a number n is n * (n-1)!
for example;
factorial of 5 is 5 * 4 * 3 * 2 * 1,
which is 5 * 4!
Same logic is used in the below function.
'''
def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
print(fact(5)) # Output: 120

