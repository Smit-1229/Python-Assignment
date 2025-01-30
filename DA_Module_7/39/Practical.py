"""
39) Write a Python program to find the second smallest number in a list. 
"""

list_1 = []

#Create a list
flag = True

while flag :
    num = int(input("Enter Number : " )  )                                 #accept element from user
    list_1.append(num)                                                              #Add element in string
    
    #Ask user to add more element or not
    choice = input("If You Want To Enter More Item Type 'y' for yes and 'n' for no : ").lower()
    if choice == 'n'or choice == "no":
        flag = False
    else :
        pass

#print list
print("list : ",list_1)

list_2 = set(list_1)
smallest_num = min(list_2)
list_2.remove(smallest_num)

smallest_num2 = min(list_2)

print("2nd smallest num in list : ",smallest_num2)

