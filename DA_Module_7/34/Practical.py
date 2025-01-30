"""
34) Write a Python function that takes two lists and returns true if they 
have at least one common member.
"""

#Create a list 1
list_1 = []
flag = True

while flag :
    string = input("Enter String For List_1 : " ).lower()                                   #accept element from user
    list_1.append(string)                                                              #Add element in string
    
    #Ask user to add more element or not
    choice = input("If You Want To Enter More Item Type 'y' for yes and 'n' for no : ").lower()
    if choice == 'n'or choice == "no":
        flag = False
    else :
        pass

#print list
print("List_1 :- ",list_1)


#Create a list 2 
list_2 = []
flag = True

while flag :
    string = input("Enter String For List_2 : " ).lower()                                   #accept element from user
    list_2.append(string)                                                              #Add element in string
    
    #Ask user to add more element or not
    choice = input("If You Want To Enter More Item Type 'y' for yes and 'n' for no : ").lower()
    if choice == 'n'or choice == "no":
        flag = False
    else :
        pass

#print list
print("List_2 :- ",list_2)


#Check if they have common element or not
flag = True
count = 0
for string in list_1:
    if string in list_2:
        count+=1
    else:
        pass

if count == 0:
    flag = False

print(flag)
       