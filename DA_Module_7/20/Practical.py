"""
20) Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string. 
"""

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Swap the first two characters of each string
new_str1 = str2[:2] + str1[2:] 
new_str2 = str1[:2] + str2[2:] 

# Combine the new strings into a single string with a space in between
result = new_str1 + " " + new_str2


print("The result after swapping the first two characters: ", result)
