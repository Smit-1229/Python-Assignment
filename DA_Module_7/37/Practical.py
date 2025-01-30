"""
37) Write a Python program to convert a list of characters into a string. 

"""

list_1 = []

#Create a list
flag = True

while flag :
    char = input("Enter Char  : " ).lower()                                   #accept element from user
    list_1.append(char)                                                              #Add element in string
    
    #Ask user to add more element or not
    choice = input("If You Want To Enter More Item Type 'y' for yes and 'n' for no : ").lower()
    if choice == 'n'or choice == "no":
        flag = False
    else :
        pass

#print list
print("list : ",list_1)

#convert list of char in string
string = "".join(list_1)

print(string)
