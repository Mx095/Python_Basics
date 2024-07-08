# Dictionary functions

# 1. dict.keys()------------------------------------------------------------------------------------------------------
# returns all keys

# Example:
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1.keys()) # dict_keys(['a', 'b', 'c'])

'''
Q1: print all the keys of the dictionary in a list
A: by using typecasting,
print(list(dict1.keys())) # Output: ['a', 'b', 'c']

Q2:  Count number of key values in the dictionary
A: by using len() function,
print(len(dict1.keys())) # Output: 3
'''

# 2. dict.values()----------------------------------------------------------------------------------------------------
# returns all values

# Example:
dict2 = {'a': 1, 'b': 2, 'c': 3}
print(dict2.values()) # dict_values([1, 2, 3])

# 3. dict.items()-----------------------------------------------------------------------------------------------------
# returns all key-value pairs as tuples -> (key,value)

# Example:
dict3 = {'a': 1, 'b': 2, 'c': 3}
print(dict3.items()) # dict_items([('a', 1), ('b', 2),('c', 3)])

# 4. dict.get("key")--------------------------------------------------------------------------------------------------
# returns the value of the key
 
# Example:
dict4 = {'a': 1, 'b': 2, 'c': 3}
print(dict4.get('a')) # Output: 1   

'''
dict.get("key") is same as dict["key"]
the only difference is,
dict.get("key") returns None if the key is not present in the dictionary. While,
dict["key"] throws an error if the key is not present in the dictionary.

*if error is thrown, then the further lines of code will not be executed
'''
dict4 = {'a': 1, 'b': 2, 'c':3}
print(dict4["a"]) # Output = 1
print(dict4.get("a")) # Output = 1

# While occurence of errors;
dict4 = {'a': 1, 'b': 2, 'c':3}
print(dict4["d"]) # Throws an error
print(dict4.get("d")) # returns None

# 5. dict.update(newDict)---------------------------------------------------------------------------------------------
# updates the key-value pair/ dictionary with the new dictionary

# Example-1: updating new key-value
dict5 = {'a': 1, 'b': 2, 'c': 3}
dict5.update({"z": 9})
print(dict5) # Output: {'a': 1, 'b': 2, 'c': 3, 'z': 9}

#Example-2: updating new dictionary 
dict5 = {'a': 1, 'b': 2, 'c': 3}
dict6 = {'d': 4, 'e': 5, 'f': 6}
dict5.update(dict6)
print(dict5) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

#Example-3: Modifying old key-value pair
dict5 = {'a': 1, 'b': 2, 'c': 3}
dict5.update({"a": 10})
print(dict5) # Output: {'a': 10, 'b': 2, 'c': 3}