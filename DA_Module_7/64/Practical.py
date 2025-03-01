"""
64) Write a Python function that checks whether a passed string is 
palindrome or not 
"""
def check_palindrome(string):
    rev_string = string[::-1].lower()
    if rev_string == string.lower():
        return f"The String ({string}) is palindrome "
    else:
        return f"The String ({string}) is not a palindrome "
    
string = input("Enter String : ")

ans = check_palindrome(string)

print(ans)