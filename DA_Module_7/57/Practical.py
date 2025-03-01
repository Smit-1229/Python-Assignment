"""
57) Write a Python program to find the highest 3 values in a dictionary
"""

dict_1 = {
    'a':10,
    'b':56,
    'c':65,
    'd':15,
    'e':95,
    'f':26,
    'g':99,
    'h':35}

sorted(dict_1)

max_3_Value = sorted(dict_1.values())

print(f"Highest 3 Value Are : {max_3_Value[-1:-4:-1]}")

