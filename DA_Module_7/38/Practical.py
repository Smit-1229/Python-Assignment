"""
38) Write a Python program to select an item randomly from a list.

"""
import random

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

random_item = random.choice(list_1)

print("Random Choice : ",random_item)
