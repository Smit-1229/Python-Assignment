"""
48) Write a Python script to sort (ascending and descending) a 
dictionary by value.
"""

dict_1 = {1:10,3:30,5:50,4:40,2:20}

dict_assend = sorted(dict_1)
print("Assending order : ")
for i in dict_assend:
    print(f"{i} : {dict_1[i]}")

print()
dict_decend = sorted(dict_1,reverse=True)
print("Decending Order : ")
for i in dict_decend:
    print(f"{i} : {dict_1[i]}")



