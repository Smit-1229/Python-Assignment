"""
75) Write a Python program to read last n lines of a file.
"""

def read_Last_N_Line(file_name,n):
    with open(file_name, "r") as file:
        lines = file.readlines()[-n:]
        return "".join(lines)

file_name = "Sample_3"
n = int(input("Enter Number Of Lines To read : "))

context = read_Last_N_Line(file_name,n)

print(context)