"""
74) Write a Python program to read first n lines of a file. 
"""

def read_Frist_N_Lines(file_name,n):
    with open(file_name, "r") as file:
        lines = file.readlines()[:n]
        return "".join(lines)
    
file_name = "Sample_3"
n = int(input("Enter Number Of Lines : "))

context = read_Frist_N_Lines(file_name,n)

print(context)