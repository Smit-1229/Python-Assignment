"""
79) Write a Python program to count the number of lines in a text file. 
"""
def count_line_in_file(file_name):
    count = 0
    with open(file_name, "r") as file:
        for line in file:
            count+=1
    return count

file_name = "Sample_3"

number_of_line = count_line_in_file(file_name)

print(f"There Are {number_of_line} Line In The File!")