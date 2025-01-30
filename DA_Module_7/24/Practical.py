"""
24) Write a Python function to insert a string in the middle of a string.

"""
#user input
string = input("Enter String : ")

#Insert String 
string_insert = input("Enter String You Want To Insert : ").lower()

#add string mid of a string
string_len_mid = len(string)//2                                                        #find mid of string

string = string[:string_len_mid] + string_insert + string[string_len_mid:]             #add string in mid

#print result
print(string)

