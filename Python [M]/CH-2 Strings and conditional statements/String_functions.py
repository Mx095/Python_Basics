#String Functions

# 1. str.endswith()-------------------------------------------------------------------------------------------------
# returns true if string ends with substr
str1 = "Hello World"
print(str1.endswith("World")) # returns True
print(str1.endswith("Universe")) # returns False
#Question : will it print the last word if function called?
#Answer : No, it will return True or False

# 2. str.capitalize()------------------------------------------------------------------------------------------------
# returns a string with the first character capitalized and the rest of the string in lowercase
str2 = "hello world"    
print(str2.capitalize()) # returns "Hello world"

# 3. str.replace(old,new)-------------------------------------------------------------------------------------------
# returns a string where all occurrences of old are replaced with new
str3 = "Hello World"
print(str3.replace("World", "Universe")) # returns "Hello Universe"
print(str3.replace("o","a")) #returns "Hella Warld"

# 4. str.find()-----------------------------------------------------------------------------------------------------
# returns the index of the first occurrence of the specified value
str4 = "Hello World"
print(str4.find("World")) # returns 6
print(str3.find("l")) # returns 2
print(str3.find("z")) # for non existing elements, returns -1 

# 5. str.count()----------------------------------------------------------------------------------------------------
# returns the number of occurrences of the specified value
str5 = "Hello World"
print(str5.count("o")) # returns 2
print(str5.count("z")) # returns 0
print(str.count("Hello")) # returns 1

