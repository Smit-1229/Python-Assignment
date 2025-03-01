"""
 
59) Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string.
"""

string = 'Hello World'

count_letter = {}

for char in string:
    if char.isalpha():
        if char.lower() in count_letter :
            count_letter[char.lower()] += 1
        else :
            count_letter[char.lower()] = 1

    
print(count_letter)

for k,v in count_letter.items():
    print(f"{k} : {v}")