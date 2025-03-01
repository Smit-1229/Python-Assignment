"""
82) Write a Python program to copy the contents of a file to another file. 
"""
def copy_file(source_file,destination_file):
    with open(source_file, "r") as sor:
        with open(destination_file,  "a") as dest:
            for line in sor:
                dest.write(line)
    
    print("The content is copy and add to another file!!")

source_file = "Sample_4"

destination_file = "Sample_5"

copy_file(source_file,destination_file)
