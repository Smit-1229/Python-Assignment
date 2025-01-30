"""
40) Write a Python program to get unique values from a list 
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

# Get unique values
unique_values = list(set(list_1))

# Print the result
print("Unique values:", unique_values)
