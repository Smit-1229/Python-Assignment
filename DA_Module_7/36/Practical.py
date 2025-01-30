"""
36) Write a Python function that takes a list and returns a new list with 
unique elements of the first list. 
"""

list_1 = []

#Create a list
flag = True

while flag :
    string = input("Enter String  : " ).lower()                                   #accept element from user
    list_1.append(string)                                                              #Add element in string
    
    #Ask user to add more element or not
    choice = input("If You Want To Enter More Item Type 'y' for yes and 'n' for no : ").lower()
    if choice == 'n'or choice == "no":
        flag = False
    else :
        pass

#print list
print("list : ",list_1)


#unique list 
unique_list = []
for word in list_1:
    if word not in unique_list:
        unique_list.append(word)
        unique_list.sort()
    else:
        pass
print(f"Unique List :- {unique_list}")