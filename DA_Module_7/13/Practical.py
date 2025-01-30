"""
Write a Python program that will return true if the two given 
integer values are equal or their sum or difference is 5. 
"""

num_1 = int(input("Enter Number 1 : "))
num_2 = int(input("Enter Number 2 : "))
status = True

if num_1 == num_2 :
    status = True
elif num_1 > num_2 :
    if num_1 - num_2 == 5 or num_1+num_2 == 5:
        status = True
    else:
        status = False
else:
    if num_2 - num_1 == 5 or num_1+num_2==5 :
        status = True
    else :
        status = False

print(status)




