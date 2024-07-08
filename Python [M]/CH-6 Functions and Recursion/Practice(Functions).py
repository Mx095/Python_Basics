# Practice programs : Functions

'''
Q1: WAF to print the length of a list. (list is the parameter)
'''
# Solution: 
cities = ["Delhi", "Gurgaon", "Noida", "Pune", "Mumbai", "Chennai"] # List-1
Movies = ["Kalki", "Salaar", "Bahubali"]

def list_length(list):
    print(len(list))

list_length(cities) # Output: 6
list_length(Movies) # Output: 7

'''
Q2: WAF to print the elements of a list in a single line. (list is the parameter)
'''
# Solution:
Movies = ["Kalki", "Salaar", "Bahubali"]

def list_elements(list):
    for element in list:
        print(element, end=" ")
    print(end = "\n") # for next question

list_elements(Movies) 
# Output:Kalki Salaar Bahubali

'''
Q3: WAF to find the factorial of n. (n is the parameter)
'''
# Solution:
def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        print(fact)

factorial(20) # Output: 2432902008176640000

'''
Q4: WAF to convert USD to INR
'''
# Solution:
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(100) # Output: 100 USD = 8300 INR

'''
Q5: WAF to print whether the given number is even or odd
'''
# Solution:
num = (int(input("Enter number: ")))
def even_odd(num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

even_odd(num)
'''
Output: 
Enter number: 2334432
2334432 is even
'''