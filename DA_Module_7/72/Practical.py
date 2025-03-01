"""
72) Write a Python program to read an entire text file. 
"""

def read_file(file_name):
    with open(file_name, "r") as file:
        context = file.read()
        return context
    
file_name = "Sample_1"
file_data = read_file(file_name)
print(file_data)