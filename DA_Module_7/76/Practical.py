"""
76) Write a Python program to read a file line by line and store it into a list 
"""

def read_store_line_in_list(file_name):
    list_file = []
    with open(file_name, "r") as file:
        for line in file:
            list_file.append(line.strip())
        return list_file

file_name = "Sample_3"

context = read_store_line_in_list(file_name)

print(context)

