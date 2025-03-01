"""
82) Write a Python program to copy the contents of a file to another file. 
"""

def copy_File(source_file,destination_file):
    with open(source_file, "r") as sor:
        content = sor.readlines()
    with open(destination_file, "a") as dest:
        dest.writelines(content)
    print("The content is copy and add to another file!!")

source_file = "Sample_4"

destination_file = "Sample_5"

copy_File(source_file,destination_file)
