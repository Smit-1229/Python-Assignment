"""
Write a Python function to reverses a string if its length is a multiple 
of 4. 
"""
#user input
string = input("Enter String : ").lower()

#if length of string is multiple of 4 reverse the string
if  len(string) % 4 == 0:
    string = string[::-1]
else:
    pass

#print result
print(string)