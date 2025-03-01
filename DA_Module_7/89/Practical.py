"""
"""

"""
=> In Python, exceptions can be handled using the try, except, and finally blocks. 
=> This structure allows you to manage errors that occur during the execution of your code and ensure cleanup or 
   necessary actions happen, regardless of whether an exception is raised.

=> Here's a breakdown of how each part works:

    --try block: Contains the code that may raise an exception.
    --except block: Handles the exception if it occurs. You can specify the type of exception to handle specific errors.
    --finally block: Contains code that will always execute, whether or not an exception occurred.
"""

#Here is an example :

try :
    num_1 = int(input("Enter Number 1 : "))
    num_2 = int(input("Enter Number 2 : "))

    ans = num_1/num_2
    print(ans)

except ValueError:
    print("Invalid Input.")

finally:
    print("Thank You For Visiting!!")