"""
31) Write a Python program to count the number of strings where the string  
length is 2 or more and the first and last character are same from a given list 
of strings. 

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
print(list_1)

#count number of string having length 2 or more and 1st & last char are same

count = 0
for word in list_1:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1
    else:
        pass

#print result
print(f"There are {count} string in list having 2 or more length and 1st & last char are same")
