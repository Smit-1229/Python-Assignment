"""
52) How Do You Check the Presence of a Key in A Dictionary?
"""

"""
=>  There are several method to check key is present or not :
    a.with get()
    b.with in operator 
    c.with in dic.key()
     
       """

dict_1 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}

key_to_check = input("Enter Key : ")

if key_to_check in dict_1:
    print(f"The Key '{key_to_check}' has the value : {dict_1[key_to_check]} ")

else:
    print(f"The key '{key_to_check}' is not present in dictionaries")    
    