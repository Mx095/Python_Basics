'''
Conversions - 2 types:
1. Implicit Conversion (Automatic Conversion) -> Type conversion
2. Explicit Conversion (Manual Conversion) -> Type casting
'''

# Type conversion -> done by system 
a = 1 #int value
b = 1.5 #float value
sum = a + b 
print(sum)

'''
 Here, considering the two inputs, float is much superior than int so the int is also converted into float
 a = 1 -> converted to 1.0 
 b = 1.5 -> remains the same 
 sum = 1.0 + 1.5 = 2.5
 gives the output as float value

 Note: here the conversion is done by the system. 
'''

# Type casting -> done by user
a = "1" #string
a = int(a) # type casting 
b = 2
sum = a + b
print(sum)

'''
first of all strings cannot be added to numbers or vice versa
so we need to convert the string into int value
a = "1" -> a = int(a) -> converted to 1
then the further calculation is done 

Note :  here the conversion is done by the user.
'''

'''
a = int("2") -- can be done
a = str(3.14) -- can be done
a = int("two") -- cannot be done
'''