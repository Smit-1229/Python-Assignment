#Write a Python program to get the Fibonacci series of given range. 
x = int(input("Start of range : "))
y = int(input("End of range : "))

a,b = 0,1

while a < y :
    a,b = b,a+b
    if a >= x and a <= y :
        print(a,end = ",")
    else:
        pass
