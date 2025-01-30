"""
32) Write a Python program to remove duplicates from a list.
"""

#Create a list
list_1 = []
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
print(list_1)

list_2 =list_1.copy()                                                               #for 2nd method


#Remove duplicate from the list
print(f"Unique List : {list(set(list_1))}")


#2nd method
unique_list = []
for word in list_2:
    if word not in unique_list:
        unique_list.append(word)
    else:
        pass

print(f"Unique List : {unique_list}")




