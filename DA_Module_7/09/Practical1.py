#Write python program that swap two number with temp variable and without temp variable. 

#With temp variable

a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))
print(f"1st number before swap :{a}")
print(f"2nd number before swap :{b}")

temp = a

a = b 
b = temp

print(f"1st number after swap :{a}")
print(f"2nd number after swap :{b}")

