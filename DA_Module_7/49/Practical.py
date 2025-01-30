"""
49) Write a Python script to concatenate following dictionaries to create 
a new one. 
"""

dict_1 = {'a':1,'b':2}
dict_2 = {'c':3,'d':4}
dict_3 = {'e':5,'f':6}

concatenate_dict = {}

concatenate_dict.update(dict_1)
concatenate_dict.update(dict_2)
concatenate_dict.update(dict_3)

print('dictionarie 1 : ',dict_1)
print('dictionarie 2 : ',dict_2)
print('dictionarie 3 : ',dict_3)
print("concatenate dictionaries : ",concatenate_dict)