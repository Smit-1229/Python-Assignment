"""
81) Write a Python program to write a list to a file. 
"""
def write_list_in_file(file_name,list_1):
    with open(file_name, "w") as file:
        for item in list_1:
            file.write(f"{item}\n")
    file.close
    return "Data Added!!"

file_name = "Sample_4"

list_1 = ["Smit : 10","Rahul : 09","Om : 08"]

result = write_list_in_file(file_name,list_1)

print(result)