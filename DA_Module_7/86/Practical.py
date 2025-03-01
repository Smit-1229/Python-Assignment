"""
86) Can one block of except statements handle multiple exception? 
"""

# Here Is An example of this : 
try :
    num_1 = int(input("Enter Number 1 : "))
    num_2 = int(input("Enter Number 2 : "))

    ans = num_1/num_2
    print(ans)

except (ZeroDivisionError,ValueError):
    print("Error Found!!, Try Agin!!")