"""
87) When is the finally block executed?
"""
#Here is an example of it : 

try :
    num_1 = int(input("Enter Number 1 : "))
    num_2 = int(input("Enter Number 2 : "))

    ans = num_1/num_2
  

except:
    print("Check The Code.")

else :
    print(ans)

finally:
    print("Thank You")