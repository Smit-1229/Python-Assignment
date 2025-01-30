# Write a Python program to get the Factorial number of given numbers. 

num = int(input("Enter Num You Want To Check : "))                #Accept num from user
fact = 1
for i in range(1,num+1):
    fact*=i

print(f"The factorial of {num} is {fact} or {num}! = {fact}")
