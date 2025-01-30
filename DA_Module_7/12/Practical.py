#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("Enter Number 1 : "))
b = int(input("Enter Number 2 : "))
c = int(input("Enter Number 3 : "))
sum = 0
if a==b or b==c or a==c:
    sum = 0
else :
    sum = a+b+c
print(f"Sum of 3 integer is {sum}")