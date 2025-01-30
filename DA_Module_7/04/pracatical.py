#Write a Python program to check if a number is positive, negative or zero

num = int(input("Enter Num You Want To Check : "))                #Accept num from user

if num < 0 :
    print(f"{num} is Negative")
elif num>0 :
    print(f"{num} is Positive ")
else:
    print("The number is zero")