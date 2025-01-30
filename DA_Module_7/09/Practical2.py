#Write python program that swap two number with temp variable and without temp variable. 

#Without temp variable

a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))
print(f"1st number before swap :{a}")
print(f"2nd number before swap :{b}")

a,b = b,a

print(f"1st number after swap :{a}")
print(f"2nd number after swap :{b}")