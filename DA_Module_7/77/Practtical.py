"""
77) Write a Python program to read a file line by line store it into a variable. 
"""

def read_store_in_variable(file_name):
    with open(file_name, "r") as file:
        context = file.read()
        return context

file_name = "Sample_3"

Variable = read_store_in_variable(file_name)

print(Variable)