"""
47) How will you create a dictionary using tuples in python?

"""

tuple_1 = (1,2,3,4,5,6,7,8,9,10)
tuple_2 = (1,4,9,16,25,36,49,64,81,100)
dict_1 = {}


for i in tuple_1:
    for j in tuple_2:
        dict_1[i] = j

print(dict_1)