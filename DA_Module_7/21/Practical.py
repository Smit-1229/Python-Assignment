"""
21) Write a Python program to add 'in' at the end of a given string (length 
should be at least 3).
If the given string already ends with 'ing' then 
add 'ly' instead if the string length of the given string is less than 3, 
leave it unchanged.

"""
#User Input
string = input("Enter String : ").lower()

#for more than 3 length
if len(string) >= 3:
    #if end with 'ing' add 'ly'
    if string.endswith("ing"):
        string = string + "ly"
    #if 'ing' is not there add 'in    
    else:
        string = string  + "in"
else:
    pass

#print result
print(string)
