"""
55) Write a Python script to merge two Python dictionaries
"""

dict_1 = {'a':1,'b':2,'c':3}
dict_2 = {'d':4,'e':5,'f':6}

merge_dict = {}

merge_dict.update(dict_1)
merge_dict.update(dict_2)

print("Dictionary 1 : ",dict_1)
print("Dictionary 2 : ",dict_2)
print("Merge Dictionary : ",merge_dict)