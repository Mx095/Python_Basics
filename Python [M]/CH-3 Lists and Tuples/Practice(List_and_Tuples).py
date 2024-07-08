# Practice programs : Lists & Tuples

# Q1 : WAP to ask the user to enter names of their 3 favourite movies & store them in a list-------------------------
# Program :
movies = []
mov1 = input("Enter 1st movie: ")
mov2 = input("Enter 2nd movie: ")
mov3 = input("Enter 3rd movie: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print("Your favourite movies are: ", movies)

# or we can directly append movies into list while taking input
movies = []
movies.append(input("Enter 1st movie: "))
movies.append(input("Enter 2nd movie: "))
movies.append(input("Enter 3rd movie: "))
print("Your favourite movies are: ", movies)

# Q2 : WAP to check if a list contains a palindrome of elements------------------------------------------------------
'''
Using copy() method
step-1 : copy the string
step-2 : reverse the copied string
step-3 : compare the original string with reversed string then determine whether it's a palindrome or not
'''
# Program-1 : int values
list = [9, 5, 9, 5, 9]

copy_list = list.copy()
copy_list.reverse()

if (copy_list == list):
    print("Palindrome")
else:
    print("Not palindrome")

# Program-2 : Strings
list = ["r", "a", "c", "e", "c", "a", "r"]

copy_list = list.copy()
copy_list.reverse()

if (copy_list == list):
    print("Palindrome")
else:
    print("Not palindrome")

# Q3 : WAP to count the number of students with "A" grade in the following tuple-------------------------------------
# Program :
grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A")) # Output : 3

# Q4: Store the above values in a list & sort them from A to D-------------------------------------------------------
# Program :
grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade) # Output : ['A', 'A', 'A', 'B', 'B', 'C]