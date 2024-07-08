# 1. String & Numeric values can operate together with * 
A,B=2,3
string="@"
print(A*string*B) 
# first step - string gets multiplied by 2 which means, string should be printed twice
# then the result gets multiplied by 3 which means, the result should be printed 3 times

#-------------------------------------------------------------------------------------------------------------------

# 2. String & String can be operate with +
A,B="2",3 # Here, 2 is taken as a variable
string="@"
print((A+string)*B)  # importance of parenthesis - calculation inside parenthesis gets done first 
# first step - A+string means, 2@ gets printed
# then the result gets multiplied by 3 which means, 2@ gets printed 3 times

#-------------------------------------------------------------------------------------------------------------------

# 3. Numeric values can operate with all arithmetic operators
A,B,C=2,3,4
print(A+B*C) 
# first step - B*C means, 3*4=12 gets (* posses higher priority than +)
# then A+12 gets calculated which means, 2+12=14 gets printed

#-------------------------------------------------------------------------------------------------------------------

# 4. Arithmetic expression with integer and float will result in float 
A,B=10,5.0
print(A*B)  # gives output as 50.0

#-------------------------------------------------------------------------------------------------------------------

# 5. Result of division operator with two integers will be float
A,B=1,2
print(A/B)  # gives output as 0.5

#-------------------------------------------------------------------------------------------------------------------

# 6. Difference between Normal division and integer  division and their outputs
A,B=1.5,3
ND=A/B
ID=A//B
print("Normal Division: ",ND) # gives output 0.5
print("Integer Division: ",ID)  # gives output as 0 but in float conversion i.e, 0.0 
# Normal division gives the exact division result
# Integer division gives the quotient in which the fractional part is discarded

#-------------------------------------------------------------------------------------------------------------------

# 7. Floor - Gives closest integer, which is lesser than or equal to the float value 
# Result of A//B = Result of floor(A/B)
# Examples:  0.1->0    5.2->5  7.99->7  -5.2->-6   5.0->5  2->2

A,B=12,5
C=A//B
print(C)
# C=12//5 -> floor(12/5) -> floor(2.4) -> 2 is the output

A,B=-12,5
C=A//B
print(C)
# C=-12//5 -> floor(-12/5) -> floor(-2.4) -> -3 is the output
# -3 is the closest integer, which is lesser than or equal to the float value

#-------------------------------------------------------------------------------------------------------------------

# 8. Remainder is negative when the denominator is negative
A,B=-12,5   
C=A%B
print(C)

A,B=5,-2
C=A%B
print(C)

#-------------------------------------------------------------------------------------------------------------------