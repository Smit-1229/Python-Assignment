"""
90) Write python program that user to enter only odd numbers, else 
will raise an exception.
"""

class evenNumberException(Exception):
    def __init__(self, *args):
        self.msg = "Invalid Input : Number Cannot Be Even "
        super().__init__(self.msg)

def check_num(num):
    if num%2 != 0 :
        print("The Number Is Odd ")
    else :
        raise evenNumberException

try:
    num = int(input("Enter A Number : "))
    check_num(num)
except evenNumberException as e:
    print(f"Error : {e}")