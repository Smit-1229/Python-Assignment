"""
85) When will the else part of try-except-else be executed?
"""

"""
Here is an example of this, there are two senario in this :
    1 - if we enter both integer number : in this the else part is excecuted 
    2 - if we enter one of them or both of them not a integer, In this senario the exception or except part is 
        excecuted and  the else part is skiped.
"""

try :
    num_1 = int(input("Enter Number 1 : "))
    num_2 = int(input("Enter Number 2 : "))

    ans = num_1/num_2
  

except:
    print("Re-Insert The Input.")

else :
    print(ans)
