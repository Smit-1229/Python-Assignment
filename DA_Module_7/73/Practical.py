"""
73) Write a Python program to append text to a file and display the text. 
"""

def append_file(file_name,data):
    with open(file_name, "a") as file:
        file.writelines(data)
        file.close()

def read_file(file_name):
    with open(file_name, "r") as file:
        context = file.read()
        return context
    
file_name = "Sample_2"
data = ["Smit\n","Rahul\n","Deep\n"]

append_file(file_name,data)
result = read_file(file_name)
print(result)