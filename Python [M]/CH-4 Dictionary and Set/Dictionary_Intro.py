# Dictionary : used to store data values in 'key:value' pairs
# They are unordered, mutable(changable) & don't allow duplicate keys
# Dictionary items are enclosed in curly brackets {}
# Syntax : dict = {key1: value1, key2: value2, ...}
'''
Example :
dict1 = {"name": "John", "age": 30, "city": "New York", "marks": [98, 97, 95]}
dict2 = {
    "name": "John",
    "age": 30,
    "city": "New York"
    "marks": [98, 97, 95]
}
'''

# Accessing dictionary elements :------------------------------------------------------------------------------------

dict1 = {"name": "John", "age": 30, "city": "New york"}
print(dict1["name"])  # Output: John
print(dict1["age"]) # Output: 30
print(dict1["city"]) # Output: New york


# Note: Both key and value can be of any data type

# Modifying dictionary elements :------------------------------------------------------------------------------------

# 1. Modifying/ Changing/ Overwriting values:
dict1 = {"name": "John", "age": 30, "city": "New york"}
dict1["age"] = 31  # Update the value of "age" key  
print(dict1)  # Output: {"name": "John", "age": 31, "city": "New york"}

# 2. Adding new values
dict1 = {"name": "John", "age": 30, "city": "New york"}
dict1["marks"] = 95  # Add a new key-value pair
print(dict1)  # Output: {"name": "John", "age": 30,  "city": "New york", "marks": 95}

# Note: empty_dictionary = {}
# empty_dictionary["key"] = "value"  # Adding a new key-value pair
# Output : {"key": "value"}

# Nested Dictionaries------------------------------------------------------------------------------------------------
# Dictionary in a dictionary
student = {
    "name": "John",
    "age": 30,
    "score": {
        "math": 98,
        "english": 97,
        "science": 95
    }
}
print(student)
# Output: {'name': 'John', 'age': 30, 'score': {'math': 98, 'english': 97, 'science': 95}}
print(student["score"])
# Output: {'math': 98, 'english': 97, 'science': 95}
print(student["score"]["math"])  # Output: 98

