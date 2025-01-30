"""
39) Write a Python program to find the second smallest number in a list. 
"""
# 2nd method

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


#by removing duplicate and then make list in order we can find smallest num 
sort_list = sorted(set(list_1))
print(f"2nd small num is : {sort_list[1]}")