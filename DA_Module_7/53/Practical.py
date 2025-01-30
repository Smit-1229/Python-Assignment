"""
53) Write a Python script to print a dictionary where the keys are 
numbers between 1 and 15.
"""

"""In the script the key is the number between 1 to 15 and value is their cube """
dict_1 = {}
for i in range(1,16):
    cube = i**3
    dict_1[i] = cube

print(dict_1)
