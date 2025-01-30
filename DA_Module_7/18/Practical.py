"""
18) Write a Python program to count occurrences of a substring in a string.
"""
string_main = input("Enter Main String : ")
sub_string = input("Enter Sub ")
count = string_main.count(sub_string)
print(f"The '{string_main}' contains '{sub_string}' {count}times. ")
