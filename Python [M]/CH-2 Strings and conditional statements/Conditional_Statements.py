# IF-ELIF-ELSE 
# Example-1-----------------------------------------------------------------------------------------------------------

light = input("light colour : ")

if (light == "red"):
    print("Stop")
elif (light == "yellow"):
    print("Wait")
elif (light == "green"):
    print("Go")
else:
    print("Light is broken")

# Example-2-----------------------------------------------------------------------------------------------------------

marks = int(input("Marks : "))

if (marks >= 90):
    print("A")
elif (marks >= 80 and marks < 90):
    print("B")
elif (marks >= 70 and marks < 80):
    print("C")
elif (marks >= 60 and marks < 70):
    print("D")
elif (marks >= 50 and marks < 60):
    print("E")
else:
    print("F")

#-------------------------------------------------------------------------------------------------------------------

#  SINGLE LINE 'IF'/ TERNARY OPERATOR 

# <var> = <val1> if <condition> else <val2>

food = input("Food : ")
eat = "Yes" if food == "cake" else "No"
print(eat)

# <St1> if <condition> else <St2>

food = input("Food : ")
print("Sweet") if food == "cake" or "jalebi" else print("Not sweet")

#-------------------------------------------------------------------------------------------------------------------

# CLEVER 'IF'/ TERNARY OPERATOR

# <VAR> = (FALSE_VAL,TRUE_VAL) [<CONDITION]

# Example-1
age = int(input())
vote = ("Yes","No") [age < 18]
print(vote)

# Example-2

'''Tax addition problem
if salary is between 0 to 50k multiply with 0.1
if salary is above 50k multiply with 0.2'''

salary = float(input("Salary : "))
tax =  salary*(0.1,0.2) [salary > 50000] 
print(tax)

#-------------------------------------------------------------------------------------------------------------------